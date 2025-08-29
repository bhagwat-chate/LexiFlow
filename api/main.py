# api/main.py

import os

from typing import Dict, List, Optional, Any
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.document_ingestion.data_ingestion import DocHandler, DocumentComparator, ChatIngestor
from src.document_analyzer.data_analysis import DocumentAnalyzer
from src.document_compare.document_comparator import DocumentCompareLLM
from src.document_chat.retrieval import ConversationalRAG
from src.document_ingestion.data_ingestion import FaissManager

# BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(title="Document Portal API", version="0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="../static"), name="static")
templates = Jinja2Templates(directory="../templates")


@app.get("/", response_class=HTMLResponse)
async def serve_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok", "service": "document-portal"}


def _read_pdf_via_handler(handler: DocHandler, path: Path)-> str:
    """
    Helper function to read pdf using DocHandler
    """
    try:
        pass
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading PDF: {str(e)}")

class FastAPIFileAdapter:
    """
    Adapt FastAPI uploads -> .name + .getbuffer() API
    """

    def __init__(self, uf: UploadFile):
        self._uf = uf
        self.name = uf.filename

    def getbuffer(self) -> bytes:
        self._uf.file.seek(0)
        return self._uf.file.read()

@app.post("/analyze")
async def analyze_document(file: UploadFile = File(...)) -> Any:
    try:
        doc_handler = DocHandler()
        saved_path = doc_handler.save_pdf(FastAPIFileAdapter(file))
        text = _read_pdf_via_handler(doc_handler, saved_path)

        analyzer = DocumentAnalyzer()
        result = analyzer.analyze_document(text)

        return JSONResponse(content=result)

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"analysis failed: {e}")


@app.post("/compare")
async def compare_documents(reference: UploadFile = File(...), actual: UploadFile = File(...)) -> Any:
    try:
        dc = DocumentComparator()
        ref_path, act_path = dc.save_uploaded_files(FastAPIFileAdapter(reference), FastAPIFileAdapter(actual))
        _ = ref_path, act_path
        combined_text = dc.combine_documents()
        comp = DocumentCompareLLM()
        df = comp.compare_documents(combined_text)

        return {"rows": df.to_dict(orient="records"), "session_id": dc.session_id}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"comparison failed: {e}")


@app.post("/chat/index")
async def chat_build_index(reference: UploadFile = File(...)) -> Any:
    try:
        pass
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"indexing failed: {e}")


@app.post("/chat/query")
async def chat_query(reference: UploadFile = File(...)) -> Any:
    try:
        pass
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"query failed: {e}")
