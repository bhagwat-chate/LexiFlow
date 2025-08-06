import os
import sys
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from dotenv import load_dotenv
from utils.model_loader import ModelLoader
from model.models import Metadata
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser
from prompt.prompt_library import prompt

log = CustomLogger().get_logger(__name__)
load_dotenv()


class DocumentAnalyzer:

    def __init__(self):
        try:
            self.loader = ModelLoader()
            self.llm = self.loader.load_model()

            self.parser = JsonOutputParser(pydantic_parser=Metadata)
            self.fixing_parser = OutputFixingParser.from_llm(parser=self.parser, llm=self.llm)

            self.prompt = prompt

            log.info("DocumentAnalyzer initialized")

        except Exception as e:
            log.error('error in initializing document analyzer')
            raise DocumentPortalException("error in initializing document analyzer", sys)

    def analyze_document(self, document_text):
        try:
            chain = self.prompt | self.llm | self.fixing_parser

            response = chain.invoke({
                "format_instructions": self.parser.get_format_instructions(),
                "document_text": document_text
            })

            log.info("metadata extraction successful", keys=list(response.keys()))

            return response

        except DocumentPortalException as e:
            log.error(f"error is metadata analysis: {str(e)}")
            raise DocumentPortalException(f"error is metadata analysis: {str(e)}", sys)
