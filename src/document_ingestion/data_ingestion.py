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
    pass


class DocHandler:
    pass


class DocumentComparator:
    pass


class ChatIngestor:
    pass


