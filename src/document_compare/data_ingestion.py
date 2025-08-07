import os
import sys
import fitz
from prompt.prompt_library import PROMPT_REGISTRY
from pathlib import Path
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from dotenv import load_dotenv

load_dotenv()


class DocumentComparator:

    def __init__(self):
        pass

    def delete_existing_files(self, file_paths):
        pass

    def save_pdf(self):
        pass

    def read_pdf(self):
        pass

