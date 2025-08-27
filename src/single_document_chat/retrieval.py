import os
import sys

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.vectorstores import FAISS
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.chains import create_history_aware_retriever
from langchain.chains import create_retrieval_chain
from langchain.chains import create_stuff_documents_chain
from dotenv import load_dotenv

from utils.model_loader import ModelLoader
from model.models import PromptType
from prompt.prompt_library import PROMPT_REGISTRY
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

load_dotenv()
log = CustomLogger.get_logger(__name__)


class ConversationalRAG:
    def __init__(self, session_id: str, retriever):
        try:
            self.session_id = session_id
            self.retriever = retriever
            self.llm = self._load_llm()
            self.contextualize_prompt = PROMPT_REGISTRY[PromptType.CONTEXTUALIZE_QUESTION.value]
            self.qa_prompt = PROMPT_REGISTRY[PromptType.CONTEXTUALIZE_QUESTION.value]
            self.history_aware_retriever = create_history_aware_retriever(self.llm, self.retriever, self.contextualize_prompt)
            log.info("created history aware retriever", session_id=self.session_id)

            self.qa_chain = create_stuff_documents_chain(self.llm, self.qa_prompt)
            self.rag_chain = create_stuff_documents_chain(self.history_aware_retriever, self.qa_chain)
            log.info("created RAG chain", session_id=self.session_id)

            self.chain = RunnableWithMessageHistory(
                self.rag_chain,
                self._get_session_history,
                input_messages_key='input',
                history_messages_key='chat_history',
                output_messages_key='answer'
            )
            log.info("created RunnableWithMessageHistory", session_id=self.session_id)

        except Exception as e:
            log.error('failed to initialize class conversationalRAG', error=str(e))
            raise DocumentPortalException('initialization error in class conversationalRAG', sys)

    def _load_llm(self):
        try:
            llm = ModelLoader().load_llm()
            log.info("llm load successful", class_name=llm.__class__.__name__)

            return llm

        except Exception as e:
            log.error('error in class conversationalRAG._load_llm()', error=str(e))
            raise DocumentPortalException('error in class conversationalRAG._load_llm()', sys)

    def _get_session_history(self, session_id: str):
        try:
            pass
        except Exception as e:
            log.error('error in class conversationalRAG._get_session_history()', error=str(e))
            raise DocumentPortalException('error in class conversationalRAG._get_session_history()', sys)

    def load_retriever_from_faiss(self, index_path: str):
        try:
            embeddings = ModelLoader().load_embedding()
            if not os.path.isdir(index_path):
                raise FileNotFoundError(f"FAISS index directory not found: {index_path}")

            vectorstore = FAISS.load_local(index_path, embeddings)
            log.info("loaded retriever from FAISS index", index_path=str(index_path))

            return vectorstore.as_retriever(search_type='similarity', search_kwargs={"k": 5})

        except Exception as e:
            log.error('error in class conversationalRAG.load_retriever_from_faiss()', error=str(e))
            raise DocumentPortalException('error in class conversationalRAG.load_retriever_from_faiss()', sys)

    def invoke(self, user_input: str) -> str:
        try:
            response = self.chain.invoke(
                input={"input": user_input},
                config={"configurable": {"session_id": self.session_id}}
            )

            answer = response.get("answer", "No answer")

            if not answer:
                log.info("Empty response received", session_id=self.session_id)

            log.info("chain invoked successfully", session_id=self.session_id, user_input=user_input, answer_preview=answer[:100])

            return answer

        except Exception as e:
            log.error('error in class conversationalRAG.invoke()', error=str(e))
            raise DocumentPortalException('error in class conversationalRAG.invoke()', sys)
