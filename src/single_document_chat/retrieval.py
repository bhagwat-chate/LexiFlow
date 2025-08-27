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


class conversationalRAG:
    def __init__(self):
        try:
            pass
        except Exception as e:
            log.error('failed to initialize class conversationalRAG', error=str(e))
            raise DocumentPortalException('initialization error in class conversationalRAG', sys)

    def _load_llm(self):
        try:
            pass
        except Exception as e:
            log.error('error in class conversationalRAG._load_llm()', error=str(e))
            raise DocumentPortalException('error in class conversationalRAG._load_llm()', sys)

    def _get_session_history(self, session_id: str):
        try:
            pass
        except Exception as e:
            log.error('error in class conversationalRAG._get_session_history()', error=str(e))
            raise DocumentPortalException('error in class conversationalRAG._get_session_history()', sys)

    def load_retriever_from_faiss(self, session_id: str):
        try:
            pass
        except Exception as e:
            log.error('error in class conversationalRAG.load_retriever_from_faiss()', error=str(e))
            raise DocumentPortalException('error in class conversationalRAG.load_retriever_from_faiss()', sys)

    def invoke(self, session_id: str):
        try:
            pass
        except Exception as e:
            log.error('error in class conversationalRAG.invoke()', error=str(e))
            raise DocumentPortalException('error in class conversationalRAG.invoke()', sys)
