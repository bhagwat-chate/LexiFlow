from src.document_analyzer.data_ingestion import DocumentHandler


if __name__ == '__main__':
    obj = DocumentHandler()
    obj.save_pdf("E:\\LLMOps\\document_portal\\data\\document_analysis\\NIPS-2017-attention-is-all-you-need-Paper.pdf")