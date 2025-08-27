import sys
import uuid
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from utils.model_loader import ModelLoader

from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

log = CustomLogger.get_logger(__name__)


class SingleDocIngestor:

    def __init__(self):
        try:
            pass
        except Exception as e:
            log.error('failed to initialize class SingleDocIngestor', error=str(e))
            raise DocumentPortalException('initialization error in class SingleDocIngestor', sys)

    def ingest_files(self):
        try:
            pass
        except Exception as e:
            log.error('failed to initialize class SingleDocIngestor.ingest_files()', error=str(e))
            raise DocumentPortalException('initialization error in class SingleDocIngestor.ingest_files()', sys)

    def create_retriever(self):
        try:
            pass
        except Exception as e:
            log.error('failed to initialize class SingleDocIngestor.create_retriever()', error=str(e))
            raise DocumentPortalException('initialization error in class SingleDocIngestor.create_retriever()', sys)
