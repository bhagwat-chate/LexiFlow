import traceback
import sys
from logger.custom_logger import CustomLogger

logger = CustomLogger().get_logger(__file__)


class DocumentPortalException(Exception):
    """Custom exception for Document Portal"""

    def __init__(self, error_message):
        self.error_message = str(error_message)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
        self.lineno = exc_tb.tb_lineno if exc_tb else -1
        self.traceback_str = ''.join(traceback.format_exception(exc_type, exc_obj, exc_tb))

    def __str__(self):
        return f"""
        Error in [{self.file_name}] at line [{self.lineno}]
        Message: {self.error_message}
        Traceback:
        {self.traceback_str}
        """
