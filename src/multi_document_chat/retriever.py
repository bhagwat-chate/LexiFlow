# src/multi_document_chat/retriever.py

import sys
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

log = CustomLogger().get_logger(__name__)


class ConversationalRAG:
    def __init__(self):
        try:
            pass
        except Exception as e:
            log.error('failed to initialize class ConversationalRAG', error=str(e))
            raise DocumentPortalException('initialization error in class ConversationalRAG', sys)

    def load_retriever_from_faiss(self):
        try:
            pass
        except Exception as e:
            log.error('error in class ConversationalRAG.load_retriever_from_faiss()', error=str(e))
            raise DocumentPortalException('error in class ConversationalRAG.load_retriever_from_faiss()', sys)

    def invoke(self):
        try:
            pass
        except Exception as e:
            log.error('error in class ConversationalRAG.invoke()', error=str(e))
            raise DocumentPortalException('error in class ConversationalRAG.invoke()', sys)

    def _load_llm(self):
        try:
            pass
        except Exception as e:
            log.error('error in class ConversationalRAG._load_llm()', error=str(e))
            raise DocumentPortalException('error in class ConversationalRAG._load_llm()', sys)

    @staticmethod
    def _format_document(docs):
        try:
            pass
        except Exception as e:
            log.error('error in class ConversationalRAG._format_document()', error=str(e))
            raise DocumentPortalException('error in class ConversationalRAG._format_document()', sys)

    def _build_lcel_chain(self):
        try:
            pass
        except Exception as e:
            log.error('error in class ConversationalRAG._build_lcel_chain()', error=str(e))
            raise DocumentPortalException('error in class ConversationalRAG._build_lcel_chain()', sys)
