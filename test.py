import os
import sys
from pathlib import Path
from src.document_analyzer.data_ingestion import DocumentHandler
from src.document_analyzer.data_analysis import DocumentAnalyzer

from exception.custom_exception import DocumentPortalException

PDF_PATH = f"E:\\LLMOps\\document_portal\\data\\document_analysis\\sample-local-pdf.pdf"


class DummyFile:
    def __init__(self, file_path):
        self.name = Path(file_path).name
        self._file_path = file_path

    def getbuffer(self):
        return open(self._file_path, "rb").read()


def main():
    try:
        # -------------------- STEP: 1 - DATA INGESTION --------------------
        print("start PDF ingestion")
        dummy_pdf = DummyFile(PDF_PATH)

        handler = DocumentHandler(session_id="test_ingestion_analysis")
        saved_path = handler.save_pdf(dummy_pdf)
        print(f"PDF saved at: {saved_path}")

        text_content = handler.read_pdf(saved_path)
        print(f"extracted data length: {len(text_content)} chars")

        # -------------------- STEP: 1 - DATA ANALYSIS --------------------
        analyzer = DocumentAnalyzer()
        analysis_result = analyzer.analyze_document(text_content)
        print("\n=== METADATA ANALYSIS RESULT ===")
        for key, value in analysis_result.items():
            print(f"{key}: {value}")

    except Exception as e:
        raise DocumentPortalException("error in system", sys)


if __name__ == '__main__':
    main()


# import io
# from pathlib import Path
# from src.document_compare.data_ingestion import DocumentIngestion
# from src.document_compare.document_comparator import DocumentCompareLLM
#
#
# def load_file_uploaded(file_path: Path):
#     return io.BytesIO(file_path.read_bytes())
#
#
# def test_compare_documents():
#     ref_path = Path("E:\\LLMOps\\document_portal\\data\document_compare\\Long_Report_V1.pdf")
#     act_path = Path("E:\\LLMOps\\document_portal\\data\document_compare\\Long_Report_V2.pdf")
#
#     class FakeUpload:
#
#         def __init__(self, file_path: Path):
#             self.name = file_path.name
#             self._buffer = file_path.read_bytes()
#
#         def getbuffer(self):
#             return self._buffer
#
#     comparator = DocumentIngestion()
#     ref_upload = FakeUpload(ref_path)
#     act_upload = FakeUpload(act_path)
#
#     ref_file, act_file = comparator.save_uploaded_files(ref_upload, act_upload)
#     combined_text = comparator.combine_documents()
#     comparator.clean_old_sessions(keep_latest=3)
#
#     print("combined text preview (first 1000 chars)")
#     print(combined_text[:1000])
#
#     llm_comparator = DocumentCompareLLM()
#     comparison_df = llm_comparator.compare_documents(combined_text)
#
#     print(f"comparison: {comparison_df}")
#
#
# if __name__ == "__main__":
#     test_compare_documents()
