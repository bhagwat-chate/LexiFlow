import os
import sys
import fitz
import uuid
from dotenv import load_dotenv
from datetime import datetime
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

load_dotenv()
log = CustomLogger().get_logger(__name__)


class DocumentHandler:
    def __init__(self, data_dir=None, session_id=None):
        try:
            self.data_dir = data_dir or os.getenv("DATA_STORAGE_PATH", os.path.join(os.getcwd(), "data", "document_analysis"))
            self.session_id = session_id or f'session_{datetime.now().strftime("%Y%m%d_%H%M%S")}_{uuid.uuid4().hex[:8]}'
            self.session_path = os.path.join(self.data_dir, self.session_id)

            os.makedirs(self.session_path, exist_ok=True)

            log.info("PDF handler initialized", session_id=self.session_id, session_path=self.session_path)

        except DocumentPortalException as e:
            log.error(f"error in initializing document handler: {str(e)}")
            raise DocumentPortalException(f"error in initializing document handler: {str(e)}", sys)

    def save_pdf(self, pdf_path):
        try:
            dest_path = os.path.join(self.session_path, f"{self.session_id}.pdf")

            with open(pdf_path, "rb") as source_file:
                with open(dest_path, "wb") as dest_file:
                    dest_file.write(source_file.read())

            log.info(f"pdf saved successfully: {dest_path}")

        except Exception as e:
            log.error(f"error in pdf save: {str(e)}")
            raise DocumentPortalException(f"error in pdf save: {str(e)}", sys)

    def read_pdf(self):
        pass


if __name__ == "__main__":
    obj = DocumentHandler()
