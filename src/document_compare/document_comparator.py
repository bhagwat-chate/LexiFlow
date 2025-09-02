# src/document_compare/document_comparator.py

import prompt.prompt_library as pl


import sys
import pandas as pd
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from prompt.prompt_library import document_comparison_prompt

from utils.model_loader import ModelLoader

from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser

log = CustomLogger().get_logger(__name__)


class DocumentCompareLLM:
    def __init__(self):
        try:
            self.loader = ModelLoader()
            self.llm = self.loader.load_model()

            self.parser = JsonOutputParser()

            self.fixing_parser = OutputFixingParser.from_llm(parser=self.parser, llm=self.llm)

            self.prompt = document_comparison_prompt

            self.chain = self.prompt | self.llm | self.fixing_parser

            log.info("DocumentCompareLLM initialized with chain, parser and model")

        except Exception as e:
            log.error(f"error in initializing DocumentCompareLLM: {str(e)}")
            raise DocumentPortalException(f"error in initializing DocumentCompareLLM: {str(e)}", sys)

    def compare_documents(self, combined_docs: str) -> pd.DataFrame:
        try:
            inputs = {
                "combined_docs": combined_docs,
                "format_instruction": self.parser.get_format_instructions(),
            }
            log.info("starting document comparison...", input_size=len(combined_docs))
            response = self.chain.invoke(inputs)
            df = pd.DataFrame(response)
            log.info("Document comparison completed", rows=len(df), columns=list(df.columns))
            return df
        except Exception as e:
            log.error(f"error in DocumentCompareLLM.compare_documents(): {str(e)}")
            raise DocumentPortalException(f"error in DocumentCompareLLM.compare_documents(): {str(e)}", sys)
