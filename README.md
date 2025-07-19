# 🧠 Document Intelligence Chat Portal

A full-stack AI-powered document analysis and comparison platform powered by advanced Retrieval-Augmented Generation (RAG) pipelines. Supports multi-document Q&A, reranking, side-by-side comparison, local LLMs, and full-stack deployment on AWS.

---

## 🚀 Key Features

### 📄 Document Ingestion & Indexing
- Supports PDF, DOCX, and unstructured text
- Metadata tagging: `title`, `page_number`, `source_id`
- Chunking via LangChain's `RecursiveCharacterTextSplitter`
- Embedding generation using: OpenAI, HuggingFace, BGE
- Vector DB support: FAISS, Chroma, Pinecone

### 💬 Conversational Intelligence
- Single-document Q&A with semantic context
- Multi-document chat via combined vector retriever
- Side-by-side document comparison (diff detection)
- Session memory and persistent chat history

### 🧠 Advanced RAG Enhancements
- Query Rewriting (e.g., RAG Fusion, ReAct)
- Context Condensation for longer prompts
- Reranking using MMR, BM25, or hybrid strategies
- Similarity metrics: Cosine, L2, Jaccard, Euclidean

### ⚙️ Performance & Optimization
- Local LLMs using `vLLM`, `Groq`, or quantized models
- Cache-Augmented Generation (CAG) for repeated queries

### 🧪 Evaluation & Testing
- RAG pipeline evaluation using precision@k, recall, MRR
- Final workflow: Upload → Ask → Compare → View Sources

---

## 🧰 Tech Stack

| Layer           | Technologies Used                                 |
|-----------------|---------------------------------------------------|
| **LLMs**        | OpenAI, HuggingFace, BGE, Groq                    |
| **RAG Framework**| LangChain (Splitters, Embedders, Retrievers)     |
| **UI Layer**    | Streamlit, Gradio                                 |
| **Backend API** | FastAPI                                           |
| **Parsing**     | PyMuPDF, PDFMiner, Unstructured, python-docx      |
| **Vector DB**   | FAISS, Chroma, Pinecone                           |
| **CI/CD**       | GitHub Actions, SonarQube                         |
| **Deployment**  | Docker, AWS ECS Fargate, ECR, IAM, SecretsMgr     |

---

## 🏗️ Project Architecture

```
document-chat-rag/
├── apps/
│   ├── frontend/              # Streamlit/Gradio UI app
│   └── backend/               # FastAPI app serving LLMs & RAG APIs
│
├── core/
│   ├── ingestion/             # File loaders, text splitters
│   ├── embeddings/            # LLM embeddings clients (OpenAI, HF, BGE)
│   ├── vector_store/          # FAISS, Chroma, Pinecone setup & search
│   ├── retrievers/            # Basic & MMR/Hybrid retrievers
│   ├── rag_logic/             # Query rewriting, RAG Fusion, rerankers
│   └── chat/                  # Session memory, chat history
│
├── utils/                     # Common helpers (formatting, logging, etc.)
├── configs/                   # YAML config for LLM, vector DB, paths
├── scripts/                   # CLI loaders, batch indexers
├── .github/
│   └── workflows/             # GitHub Actions for CI/CD
├── Dockerfile                 # Docker container definition
├── docker-compose.yml         # (Optional) Local dev setup
├── requirements.txt           # Python dependencies
└── README.md                  # Project overview
```

---

## ⚙️ CI/CD & Deployment on AWS

- **CI/CD via GitHub Actions**
  - Auto-trigger build on PR or `release/*` branch push
  - Linting, testing, SonarQube static analysis
  - Docker image build + push to AWS ECR

- **AWS Deployment Stack**
  - ECS Fargate for container hosting
  - Secrets via AWS Secrets Manager
  - ECR for Docker images
  - IAM roles for secure access
  - Environment config via GitHub + AWS CLI

---

## 🧪 Evaluation

- Evaluate RAG with standard metrics:
  - `precision@k`, `recall`, `MRR`, `response relevance`
- Document comparison analysis:
  - Track overlap and differences in model answers
  - Visual highlight of matched/mismatched responses

---

## 📦 Local Setup & Run

```bash
# 1. Clone the repo
git clone https://github.com/bhagwat-chate/document_portal/tree/release/1.0/dev/bhagwat
cd document-chat-rag

# 2. Setup virtual environment
python -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run backend (FastAPI)
cd apps/backend
uvicorn main:app --reload

# 5. Run frontend (Streamlit or Gradio)
cd ../frontend
streamlit run app.py
```

---

## 🧠 Future Enhancements

- 🧾 PDF export of Q&A sessions
- 👥 Multi-user access with login & token-based sessions
- 🧩 Support for Google Drive/Dropbox as input source
- 📊 Admin dashboard for usage analytics
- 🔄 Feedback loop with human-in-the-loop evaluation

---

## 🤝 Contribution

Feel free to open issues, submit PRs, or suggest improvements. This project aims to be production-grade and extensible.

---

## 📄 License

[MIT License](LICENSE)

---

**Built with ❤️ for intelligent document understanding.**
