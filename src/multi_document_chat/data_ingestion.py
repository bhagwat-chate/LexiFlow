# src/multi_document_chat/data_ingestion.py

import sys
import uuid
from pathlib import Path
from datetime import datetime, timezone
from utils.model_loader import ModelLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import TextLoader
from langchain.document_loaders import Docx2txtLoader
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

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

            self.SUPPORTED_EXTENSIONS = {'.pdf', '.docx', '.txt', '.md'}

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

    def ingest_files(self, uploaded_files):
        try:
            documents = []

            for uploaded_file in uploaded_files:

                ext = Path(uploaded_file.name).suffix.lower()

                if ext not in self.SUPPORTED_EXTENSIONS:
                    log.warning(f"unsupported file skipped. ", filename=uploaded_file.name)
                    continue

                file_name = f"{uuid.uuid4().hex[:8]}{ext}"
                temp_path = self.session_temp_dir / file_name

                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.read())

                log.info(f'file saved for ingestion', file_name=file_name, saved_at=str(temp_path), session_id=str(self.session_id))

                if ext == '.pdf':
                    loader = PyPDFLoader(str(temp_path))
                elif ext == '.docx':
                    loader = Docx2txtLoader(str(temp_path))
                elif ext == '.txt':
                    loader = TextLoader(str(temp_path), encoding='utf-8')
                else:
                    log.warning(f"unsupported file type encountered. ", filename=uploaded_file.name)
                    continue

                docs = loader.load()
                documents.extend(docs)

                if not documents:
                    raise DocumentPortalException("no valid documents loaded.", sys)

                return self._create_retrieval(documents)

        except Exception as e:
            log.error('error in class DocumentIngestor.ingest_files()', error=str(e))
            raise DocumentPortalException('error in class DocumentIngestor.ingest_files()', sys)

    def _create_retrieval(self, documents):
        try:
            pass
        except Exception as e:
            log.error('error in class DocumentIngestor._create_retrieval()', error=str(e))
            raise DocumentPortalException('error in class DocumentIngestor._create_retrieval()', sys)
