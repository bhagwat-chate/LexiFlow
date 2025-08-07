import os
import sys
import fitz
from prompt.prompt_library import PROMPT_REGISTRY
from pathlib import Path
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from dotenv import load_dotenv

load_dotenv()
log = CustomLogger().get_logger(__name__)


class DocumentIngestion:

    def __init__(self, base_dir):
        try:
            self.base_dir = Path(base_dir)
            self.base_dir.mkdir(parents=True, exist_ok=True)

        except Exception as e:
            log.error(f"error in initializing DocumentIngestion: {str(e)}")
            raise DocumentPortalException(f"error in initializing DocumentIngestion: {str(e)}", sys)

    def delete_existing_files(self, file_paths):
        try:

            pass

        except Exception as e:
            log.error(f"error in delete_existing_files: {str(e)}")
            raise DocumentPortalException(f"error in delete_existing_files: {str(e)}", sys)

    def save_pdf(self):
        try:

            pass

        except Exception as e:
            log.error(f"error in save_pdf: {str(e)}")
            raise DocumentPortalException(f"error in save_pdf: {str(e)}", sys)

    def read_pdf(self, pdf_path: Path) -> str:
        try:

            with fitz.open(self, pdf_path) as doc:
                if doc.is_encrypted():
                    raise ValueError("PDF is encrypted and can not be read")

                all_text = []

                for page_num in range(len(doc.page_count)):
                    page = doc.load_page(page_num)
                    text = page.get_text()

                    if text.strip():
                        all_text.append(f"\n --- Page {page_num + 1} --- \n {text}")

            log.info("PDF read successful", file=str(pdf_path), pages=len(all_text))

            return "\n".join(all_text)

        except Exception as e:
            log.error(f"error in read_pdf: {str(e)}")
            raise DocumentPortalException(f"error in read_pdf: {str(e)}", sys)
