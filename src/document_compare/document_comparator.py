import os
import sys
import pandas as pd
from dotenv import load_dotenv
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import ChangeFormat, SummaryResponse
from prompt.prompt_library import PROMPT_REGISTRY
from utils.model_loader import ModelLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser

load_dotenv()
log = CustomLogger().get_logger(__name__)


class DocumentCompareLLM:
    def __init__(self):
        try:
            self.loader = ModelLoader()
            self.llm = self.loader.load_model()
            self.parser = JsonOutputParser()
            self.fixing_parser = OutputFixingParser(parser=self.parser, llm=self.llm)
            self.prompt = PROMPT_REGISTRY['document_comparison_prompt']
            self.chain = self.prompt | self.llm | self.parser | self.fixing_parser

            log.info("DocumentCompareLLM initialized with chain, parser and model")
        except Exception as e:
            log.erroe(f"error in initializing DocumentCompareLLM: {str(e)}")
            raise DocumentPortalException(f"error in initializing DocumentCompareLLM: {str(e)}", sys)

    def compare_documents(self):
        pass

    def _format_response(self):
        pass
