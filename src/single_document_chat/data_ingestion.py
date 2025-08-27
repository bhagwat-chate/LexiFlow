import sys
import uuid
from pathlib import Path
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from utils.model_loader import ModelLoader
from datetime import datetime
from datetime import timezone

from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

log = CustomLogger().get_logger(__name__)


class SingleDocIngestor:

    def __init__(self, data_dir: str = 'data/single_document_chat', faiss_dir: str = 'faiss_index'):
        try:
            self.data_dir = Path(data_dir)
            self.data_dir.mkdir(parents=True, exist_ok=True)
            self.file_path = self.data_dir / f"{uuid.uuid4()}.pdf"

            self.faiss_dir = Path(faiss_dir)
            self.faiss_dir.mkdir(parents=True, exist_ok=True)

            self.model_loader = ModelLoader()

            log.info("class SingleDocIngestor initialized with", temp_path=str(self.data_dir), faiss_path=str(self.faiss_dir))

        except Exception as e:
            log.error('failed to initialize class SingleDocIngestor', error=str(e))
            raise DocumentPortalException('initialization error in class SingleDocIngestor', sys)

    def ingest_files(self, uploaded_files):
        try:
            documents = []

            for uploaded_file in uploaded_files:
                unique_filename = f"session_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}.pdf"
                temp_path = self.data_dir / unique_filename

                with open(temp_path, "wb") as f_out:
                    f_out.write(uploaded_file.read())

                log.info("PDF saved for ingestion", filename=uploaded_file.name)

                loader = PyPDFLoader(str(temp_path))
                docs = loader.load()
                documents.extend(docs)

            log.info("PDF files loaded", count=len(documents))

            return self.create_retriever(documents)

        except Exception as e:
            log.error('error is class SingleDocIngestor.ingest_files()', error=str(e))
            raise DocumentPortalException('error in class SingleDocIngestor.ingest_files()', sys)

    def create_retriever(self, documents: List):
        try:
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=300)
            chunks = splitter.split_documents(documents)
            log.info(f"chunks created from documents. total chunks: {len(chunks)}")

            embeddings = self.model_loader.load_embedding()
            vectorstore = FAISS.from_documents(documents=chunks, embedding=embeddings)
            vectorstore.save_local(str(self.faiss_dir))
            log.info("FAISS index created and saved", faiss_path=str(self.faiss_dir))

            retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
            log.info("retriever created successfully", faiss_path=str(self.faiss_dir))

            return retriever

        except Exception as e:
            log.error('error in class SingleDocIngestor._create_retriever()', error=str(e))
            raise DocumentPortalException('error in class SingleDocIngestor._create_retriever()', sys)
