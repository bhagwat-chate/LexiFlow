# src/multi_document_chat/retriever.py

import os
import sys

from typing import List, Optional
from operator import itemgetter
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import FAISS
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

from utils.model_loader import ModelLoader
from prompt.prompt_library import PROMPT_REGISTRY
from model.models import PromptType

from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

log = CustomLogger().get_logger(__name__)


class ConversationalRAG:
    def __init__(self, session_id: str, retriever=None):
        try:
            self.session_id = session_id
            self.retriever = retriever
            self.llm = self._load_llm()
            self.contextualize_prompt = PROMPT_REGISTRY[PromptType.CONTEXTUALIZE_QUESTION.value]
            self.qa_prompt: ChatPromptTemplate = PROMPT_REGISTRY[PromptType.CONTEXT_QA.value]

            if not retriever:
                raise ValueError("retriever can not ba None")
            self.retriever = retriever
            self._build_lcel_chain()

            log.info("ConversationalRAG initialized", session_id=self.session_id)

        except Exception as e:
            log.error('failed to initialize class ConversationalRAG', error=str(e))
            raise DocumentPortalException('initialization error in class ConversationalRAG', sys)

    def load_retriever_from_faiss(self, index_path: str):
        try:
            embeddings = ModelLoader().load_embedding()

            if not os.path.isdir(index_path):
                raise FileNotFoundError(f"FAISS index file not found: ", {index_path})

            vector_store = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

            self.retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})

            log.info("FAISS retriever loaded", index_apth=index_path, session_id=self.session_id)

            self._build_lcel_chain()

            return self.retriever

        except Exception as e:
            log.error('error in class ConversationalRAG.load_retriever_from_faiss()', error=str(e))
            raise DocumentPortalException('error in class ConversationalRAG.load_retriever_from_faiss()', sys)

    def invoke(self, user_input: str, chat_history: Optional[List[BaseMessage]] = None) -> str:
        try:

            chat_history = chat_history or []
            payload = {"input": user_input, "chat_history": chat_history}

            response = self.chain.invoke(payload)

            if not response:
                log.warning(f"no answer generated", user_input=user_input, session_id=self.session_id)
                return "no answer generated"

            log.info("chain invoked successfully", session_id=self.session_id, user_input=user_input, answer_preview=response[:100])

            return response

        except Exception as e:
            log.error('error in class ConversationalRAG.invoke()', error=str(e))
            raise DocumentPortalException('error in class ConversationalRAG.invoke()', sys)

    def _load_llm(self):
        try:
            llm = ModelLoader().load_llm()

            if not llm:
                raise ValueError("LLM could not be loaded")

            log.info("LLM loaded successfully", session_id=self.session_id)

            return llm

        except Exception as e:
            log.error('error in class ConversationalRAG._load_llm()', error=str(e))
            raise DocumentPortalException('error in class ConversationalRAG._load_llm()', sys)

    @staticmethod
    def _format_docs(docs):
        try:
            return "\n\n".join(d.page_content for d in docs)

        except Exception as e:
            log.error('error in class ConversationalRAG._format_document()', error=str(e))
            raise DocumentPortalException('error in class ConversationalRAG._format_document()', sys)

    def _build_lcel_chain(self):
        try:

            # Rewrite the user question using chat history
            question_rewriter = (
                    {
                        "input": itemgetter("input"),
                        "chat_history": itemgetter("chat_history"),
                    }
                    | self.contextualize_prompt
                    | self.llm
                    | StrOutputParser()
            )

            # Retrieve docs for the rewritten question and format them
            retrieve_docs = (
                    question_rewriter
                    | self.retriever
                    | RunnableLambda(self._format_docs)
            )

            # Build the QA chain
            self.chain = (
                    {
                        "context": retrieve_docs,
                        "question": itemgetter("input"),
                        "chat_history": itemgetter("chat_history"),
                    }
                    | self.qa_prompt
                    | self.llm
                    | StrOutputParser()
            )

            self._chain_ready = True

            log.info(f"chain created", session_id=self.session_id)

        except Exception as e:
            log.error('error in class ConversationalRAG._build_lcel_chain()', error=str(e))
            raise DocumentPortalException('error in class ConversationalRAG._build_lcel_chain()', sys)
