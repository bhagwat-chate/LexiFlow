import os
import sys
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from dotenv import load_dotenv
from utils.model_loader import ModelLoader
from model.models import *
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser

log = CustomLogger().get_logger(__name__)
load_dotenv()


class DocumentAnalyzer:

    def __init__(self):
        pass

    def analysis_metadata(self):
        try:
            pass

        except DocumentPortalException as e:
            log.error(f"error is metadata analysis: {str(e)}")
            raise DocumentPortalException(f"error is metadata analysis: {str(e)}", sys)
