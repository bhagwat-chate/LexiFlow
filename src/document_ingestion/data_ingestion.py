from __future__ import annotations
import os
import sys
import fitz
import json
import uuid
import shutil
import hashlib
from pathlib import Path
from datetime import datetime
from datetime import timezone
from typing import List, Optional, Dict, Any

from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.vectorstores import FAISS

from utils.model_loader import ModelLoader
# from utils.file_io import _session_id, save_uploaded_files
# from utils.document_ops import load_documents, concat_for_analysys, concat_for_cpmparison

from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

log = CustomLogger().get_logger(__name__)


class FaissManager:
    def __init__(self):
        try:
            pass
        except Exception as e:
            log.info(f"class FaissManager initialization failed")
            raise DocumentPortalException(f"class FaissManager initialization failed: {str(e)}", sys)

    def _exists(self):
        try:
            pass
        except Exception as e:
            log.info(f"error in FaissManager()._exists()")
            raise DocumentPortalException(f"error in FaissManager()._exists(): {str(e)}", sys)

    @staticmethod
    def _fingerprint():
        try:
            pass
        except Exception as e:
            log.info(f"error in FaissManager()._exists()")
            raise DocumentPortalException(f"error in FaissManager()._exists(): {str(e)}", sys)

    def _save_meta(self):
        try:
            pass
        except Exception as e:
            log.info(f"error in FaissManager()._save_meta()")
            raise DocumentPortalException(f"error in FaissManager()._save_meta(): {str(e)}", sys)

    def add_documents(self):
        try:
            pass
        except Exception as e:
            log.info(f"error in FaissManager().add_documents()")
            raise DocumentPortalException(f"error in FaissManager().add_documents(): {str(e)}", sys)

    def load_or_create(self):
        try:
            pass
        except Exception as e:
            log.info(f"error in FaissManager().load_or_create()")
            raise DocumentPortalException(f"error in FaissManager().load_or_create(): {str(e)}", sys)


class DocHandler:
    def __init__(self):
        try:
            pass
        except Exception as e:
            log.info(f"class DocHandler initialization failed")
            raise DocumentPortalException(f"class DocHandler initialization failed: {str(e)}", sys)

    def save_pdf(self):
        try:
            pass
        except Exception as e:
            log.info(f"error in DocHandler().save_pdf()")
            raise DocumentPortalException(f"error in DocHandler().save_pdf(): {str(e)}", sys)

    def read_pdf(self):
        try:
            pass
        except Exception as e:
            log.info(f"error in DocHandler().read_pdf()")
            raise DocumentPortalException(f"error in DocHandler().read_pdf(): {str(e)}", sys)


class DocumentComparator:
    def __init__(self):
        try:
            pass
        except Exception as e:
            log.info(f"class DocumentComparator initialization failed")
            raise DocumentPortalException(f"class DocumentComparator initialization failed: {str(e)}", sys)

    def save_uploaded_files(self):
        try:
            pass
        except Exception as e:
            log.info(f"error in DocumentComparator().save_uploaded_files()")
            raise DocumentPortalException(f"error in DocumentComparator().save_uploaded_files(): {str(e)}", sys)

    def read_pdf(self):
        try:
            pass
        except Exception as e:
            log.info(f"error in DocumentComparator().read_pdf()")
            raise DocumentPortalException(f"error in DocumentComparator().read_pdf(): {str(e)}", sys)

    def cpmbine_documents(self):
        try:
            pass
        except Exception as e:
            log.info(f"error in DocumentComparator().cpmbine_documents()")
            raise DocumentPortalException(f"error in DocumentComparator().cpmbine_documents(): {str(e)}", sys)

    def clean_old_sessions(self):
        try:
            pass
        except Exception as e:
            log.info(f"error in DocumentComparator().clean_old_sessions()")
            raise DocumentPortalException(f"error in DocumentComparator().clean_old_sessions(): {str(e)}", sys)


class ChatIngestor:
    def __init__(self):
        try:
            pass
        except Exception as e:
            log.info(f"class ChatIngestor initialization failed")
            raise DocumentPortalException(f"class ChatIngestor initialization failed: {str(e)}", sys)

    def _resolve_dir(self):
        try:
            pass
        except Exception as e:
            log.info(f"error in ChatIngestor()._resolve_dir()")
            raise DocumentPortalException(f"error in ChatIngestor()._resolve_dir(): {str(e)}", sys)

    def _split(self):
        try:
            pass
        except Exception as e:
            log.info(f"error in ChatIngestor()._split()")
            raise DocumentPortalException(f"error in ChatIngestor()._split(): {str(e)}", sys)

    def built_retriver(self):
        try:
            pass
        except Exception as e:
            log.info(f"error in ChatIngestor().built_retriever()")
            raise DocumentPortalException(f"error in ChatIngestor().built_retriever(): {str(e)}", sys)
