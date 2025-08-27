# src/multi_document_chat/data_ingestion.py

import sys
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

log = CustomLogger().get_logger(__name__)


class DocumentIngestor:
    def __init__(self):
        try:
            pass
        except Exception as e:
            log.error('failed to initialize class DocumentIngestor', error=str(e))
            raise DocumentPortalException('initialization error in class DocumentIngestor', sys)

    def ingest_files(self):
        try:
            pass
        except Exception as e:
            log.error('error in class DocumentIngestor.ingest_files()', error=str(e))
            raise DocumentPortalException('error in class DocumentIngestor.ingest_files()', sys)

    def _create_retrieval(self, documents):
        try:
            pass
        except Exception as e:
            log.error('error in class DocumentIngestor._create_retrieval()', error=str(e))
            raise DocumentPortalException('error in class DocumentIngestor._create_retrieval()', sys)
