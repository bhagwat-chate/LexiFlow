# import os
# import sys
# from pathlib import Path
# from src.document_analyzer.data_ingestion import DocumentHandler
# from src.document_analyzer.data_analysis import DocumentAnalyzer
#
# from exception.custom_exception import DocumentPortalException
#
# PDF_PATH = f"E:\\LLMOps\\document_portal\\data\\document_analysis\\sample-local-pdf.pdf"
#
#
# class DummyFile:
#     def __init__(self, file_path):
#         self.name = Path(file_path).name
#         self._file_path = file_path
#
#     def getbuffer(self):
#         return open(self._file_path, "rb").read()
#
#
# def main():
#     try:
#         # -------------------- STEP: 1 - DATA INGESTION --------------------
#         print("start PDF ingestion")
#         dummy_pdf = DummyFile(PDF_PATH)
#
#         handler = DocumentHandler(session_id="test_ingestion_analysis")
#         saved_path = handler.save_pdf(dummy_pdf)
#         print(f"PDF saved at: {saved_path}")
#
#         text_content = handler.read_pdf(saved_path)
#         print(f"extracted data length: {len(text_content)} chars")
#
#         # -------------------- STEP: 1 - DATA ANALYSIS --------------------
#         analyzer = DocumentAnalyzer()
#         analysis_result = analyzer.analyze_document(text_content)
#         print("\n=== METADATA ANALYSIS RESULT ===")
#         for key, value in analysis_result.items():
#             print(f"{key}: {value}")
#
#     except Exception as e:
#         raise DocumentPortalException("error in system", sys)
#
#
# if __name__ == '__main__':
#     main()

# testing code for doc compare
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

# Testing code for single doc chat

import os
import sys
from pathlib import Path
from langchain_community.vectorstores import FAISS
from src.single_document_chat.data_ingestion import SingleDocIngestor
from src.single_document_chat.retrieval import ConversationalRAG
from utils.model_loader import ModelLoader

FAISS_INDEX_PATH = Path("faiss_index")


def test_conversational_rag_with_pdf(pdf_path: str, question: str):
    try:
        model_loader = ModelLoader()

        if FAISS_INDEX_PATH.exists():
            print("loading the FAISS index")

            embeddings = model_loader.load_embedding()
            vector_store = FAISS.load_local(str(FAISS_INDEX_PATH), embeddings=embeddings, allow_dangerous_deserialization=True)
            retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k': 5})

        else:
            print("FAISS index not found. Ingesting the PDF and creating index...")
            with open(pdf_path, "rb") as file:
                uploaded_files = [file]
                ingestor = SingleDocIngestor()
                retriever = ingestor.ingest_files(uploaded_files)
        print("running conversational RAG...")
        session_id = "test_rag"
        rag = ConversationalRAG(session_id, retriever)

        response = rag.invoke(question)
        print(f"\n Question: {question}\n Answer: {response}")

    except Exception as e:
        print(f"TEST FAILED: {e}")
        sys.exit(1)


if __name__ == "__main__":
    pdf_path = "E:\\LLMOps\\document_portal\\data\\single_document_chat\\NIPS-2017-attention-is-all-you-need-Paper.pdf"
    question = "What is the attention mechanism, explain me in 60 words?"

    if not Path(pdf_path).exists():
        print(f"PDF file does not exist: {pdf_path}")
        sys.exit(1)

    test_conversational_rag_with_pdf(pdf_path, question)
