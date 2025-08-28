# src/multi_document_chat/data_ingestion.py

import sys
from pathlib import Path
import uuid
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from datetime import datetime, timezone
from utils.model_loader import ModelLoader
log = CustomLogger().get_logger(__name__)


class DocumentIngestor:

    SUPPORTED_EXTENSIONS = {'.pdf', '.docx', '.txt', '.md'}

    def __init__(self, temp_dir: str = 'data/multi_doc_chat', faiss_dir: str = 'faiss_index', session_id: str | None = None):
        try:
            self.temp_dir = Path(temp_dir)
            self.temp_dir.mkdir(parents=True, exist_ok=True)

            self.faiss_dir = Path(faiss_dir)
            self.faiss_dir.mkdir(parents=True, exist_ok=True)

            self.session_id = session_id or f"session_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"
            self.session_temp_dir = self.temp_dir / self.session_id
            self.session_faiss_dir = self.faiss_dir / self.session_id
            self.session_temp_dir.mkdir(parents=True, exist_ok=True)
            self.session_faiss_dir.mkdir(parents=True, exist_ok=True)

            self.model_loader = ModelLoader()

            log.info("initialized the class DocumentIngestor",
                     base_temp_dir=str(self.temp_dir),
                     base_faiss_dir=str(self.faiss_dir),
                     session_id=str(self.session_id),
                     session_temp_dir=str(self.session_temp_dir),
                     session_faiss_dir=str(self.session_faiss_dir)
                     )

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
