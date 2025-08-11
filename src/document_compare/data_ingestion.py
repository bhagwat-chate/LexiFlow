# src/document_compare/data_ingestion.py

import sys
import fitz
from pathlib import Path
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

log = CustomLogger().get_logger(__name__)


class DocumentIngestion:
    def __init__(self, base_dir: str = r"data\document_compare"):
        try:
            self.base_dir = Path(base_dir)
            self.base_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            log.error(f"error in initializing DocumentIngestion: {str(e)}")
            raise DocumentPortalException(f"error in initializing DocumentIngestion: {str(e)}", sys)

    def delete_existing_files(self) -> None:
        try:
            if self.base_dir.exists() and self.base_dir.is_dir():
                for file in self.base_dir.iterdir():
                    if file.is_file() and file.suffix.lower() == ".pdf":
                        file.unlink()
                        log.info("file deleted", path=str(file))
                log.info("directory_cleaned", directory=str(self.base_dir))
        except Exception as e:
            log.error(f"error in delete_existing_files: {str(e)}")
            raise DocumentPortalException(f"error in delete_existing_files: {str(e)}", sys)

    def save_uploaded_files(self, reference_file, actual_file):
        try:
            self.delete_existing_files()
            log.info("existing files deleted successfully")

            if not reference_file.name.lower().endswith(".pdf") or not actual_file.name.lower().endswith(".pdf"):
                raise ValueError("only pdf files are allowed.")

            ref_path = self.base_dir / reference_file.name
            act_path = self.base_dir / actual_file.name

            with open(ref_path, "wb") as f:
                f.write(reference_file.getbuffer())
            with open(act_path, "wb") as f:
                f.write(actual_file.getbuffer())

            log.info("files saved", reference=str(ref_path), actual=str(act_path))

            return ref_path, act_path

        except Exception as e:
            log.error(f"error in save_pdf: {str(e)}")
            raise DocumentPortalException(f"error in save_pdf: {str(e)}", sys)

    def read_pdf(self, pdf_path: Path) -> str:
        try:
            with fitz.open(pdf_path) as doc:
                if doc.is_encrypted:
                    raise ValueError("PDF is encrypted and can not be read")

                pages_text = []
                for page_num in range(len(doc)):
                    page = doc.load_page(page_num)
                    text = page.get_text("text")
                    if text.strip():
                        pages_text.append(f"\n--- Page {page_num + 1} ---\n{text}")

            log.info("PDF read successful", file=str(pdf_path), pages=len(pages_text))
            return "\n".join(pages_text)

        except Exception as e:
            log.error(f"error in read_pdf: {str(e)}")
            raise DocumentPortalException(f"error in read_pdf: {str(e)}", sys)

    def combine_documents(self) -> str:
        try:
            parts = []
            for filename in sorted(self.base_dir.iterdir()):
                if filename.is_file() and filename.suffix.lower() == ".pdf":
                    content = self.read_pdf(filename)
                    parts.append(f"Document: {filename.name}\n{content}")

            combined_text = "\n\n".join(parts)
            log.info("Documents combined", num_docs=len(parts), total_chars=len(combined_text))
            return combined_text

        except Exception as e:
            log.error(f"error in DocumentIngestion.combine_documents(): {str(e)}")
            raise DocumentPortalException(f"error in DocumentIngestion.combine_documents(): {str(e)}", sys)
