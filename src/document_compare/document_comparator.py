import os
import sys
import pandas as pd
from dotenv import load_dotenv
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import ChangeFormat, SummaryResponse
from prompt.prompt_library import PROMPT_REGISTRY
from utils.model_loader import load_config
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser

load_dotenv()

log = CustomLogger().get_logger(__name__)


class DocumentCompareLLM:
    def __init__(self):
        pass

    def compare_documents(self):
        pass

    def _format_response(self):
        pass
