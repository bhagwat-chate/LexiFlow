# 📄 Document Portal – Intelligent PDF Chat, Analysis & Comparison Platform

[![Python](https://img.shields.io/badge/Python-3.11.7-blue.svg)](https://www.python.org/downloads/release/python-3117/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 🚀 Overview

**Document Portal** is a production-grade GenAI platform designed to **analyze**, **compare**, and **converse** over PDF documents using state-of-the-art LLMs and retrieval-augmented generation (RAG) pipelines.

This platform enables enterprises, legal teams, researchers, and policy analysts to:
- 🧠 Extract insights from complex documents
- 🔍 Track changes between document versions
- 💬 Chat intelligently with single or multiple PDFs
- ⚙️ Configure and switch between multiple LLMs and embedding models dynamically

---

## 🧠 Core Features

| Feature                 | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| 📂 `document_analyzer`  | Extracts metadata such as title, author, pages, and a concise summary       |
| 🆚 `document_compare`   | Compares two PDF documents and identifies key changes or differences         |
| 💬 `single_document_chat` | Query and chat over a single PDF document using semantic search + LLM       |
| 🗂️ `multi_document_chat` | Chat with multiple uploaded PDFs contextually via top-k retrieval            |

> ⚠️ **Currently Supported Format**: `.pdf` only  
> 🧩 Future formats (docx, txt, OCR scans) will be added in upcoming versions.

---

## ⚙️ Tech Stack

| Layer         | Technology                                      |
|---------------|--------------------------------------------------|
| Language      | Python 3.11.7                                    |
| Core Logic    | LangChain, Pydantic                              |
| LLMs          | OpenAI GPT-4o, Google Gemini, Groq DeepSeek      |
| Embeddings    | OpenAI `text-embedding-3-small`, Google `004`    |
| Vector Store  | Qdrant                                           |
| Storage       | AWS S3 (for production), Local Disk (for dev)    |
| Deployment    | Docker, AWS EC2, FastAPI, CloudWatch             |

---

## 📁 Project Structure

```
document_portal/
├── main.py
├── test.py
├── .env
├── configs/
│   └── config.yaml
├── src/
│   └── document_analyzer/
│       ├── data_ingestion.py
│       ├── analyzer.py
│       ├── compare.py
│       ├── chat_single.py
│       ├── chat_multi.py
├── utils/
│   ├── config_loader.py
│   ├── logger/
│   │   └── custom_logger.py
│   └── exception/
│       └── custom_exception.py
├── data/
│   └── document_analysis/
├── logs/
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🔧 Configuration – `config.yaml`

### ✅ Embedding Models

```yaml
embedding_model:
  google:
    provider: "google"
    model_name: "models/text-embedding-004"

  openai:
    provider: "openai"
    model_name: "text-embedding-3-small"
```

---

### 🧠 LLM Models

```yaml
llm:
  groq:
    provider: "groq"
    model_name: "deepseek-r1-distill-llama-70b"
    temperature: 0
    max_output_tokens: 2048

  google:
    provider: "google"
    model_name: "gemini-2.0-flash"
    temperature: 0
    max_output_tokens: 2048

  openai:
    provider: "openai"
    model_name: "gpt-4o"
    temperature: 0.0
    max_output_tokens: 2048
```

---

### 🔁 Retriever

```yaml
retriever:
  top_k: 10
```

---

### 📂 Qdrant Vector Store

```yaml
qdrant_db:
  host: "localhost"
  port: 6333
  collection_name: "document_portal"
```

---

## 📦 Environment Variables – `.env`

```dotenv
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
DATA_STORAGE_PATH=./data/document_analysis
```

---

## 🧰 Usage Instructions

### 1️⃣ Clone and Setup

```bash
git clone https://github.com/bhagwat-chate/document_portal.git
cd document_portal
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2️⃣ Configure `.env` and `config.yaml`

> Make sure your `.env` and `configs/config.yaml` are updated with valid credentials and model configs.

---

### 3️⃣ Run Main Program

```bash
python main.py
```

---

## 🐳 Docker Deployment

### 🛠️ Build Docker Image

```bash
docker build -t document-portal .
```

### ▶️ Run with Docker Locally

```bash
docker run -p 8000:8000 --env-file .env document-portal
```

---

## ☁️ AWS Deployment Strategy

| Component       | Description                                                  |
|-----------------|--------------------------------------------------------------|
| **EC2 Instance**| Hosts the Docker container (Ubuntu + Docker + FastAPI)       |
| **S3 Bucket**   | Stores uploaded documents per user/session                   |
| **IAM Role**    | Fine-grained access to S3 + secrets                          |
| **CloudWatch**  | For application-level logging and monitoring                 |
| **API Gateway** | (Optional) External-facing HTTPS interface                   |

---

## ✅ Feature Checklist

- [x] Upload + Save PDFs in session-specific folders
- [x] Extract metadata: title, author, pages, summary
- [x] Query documents with context-aware RAG
- [x] Chat with one or multiple PDFs
- [x] Configurable LLM/embedding via YAML
- [ ] FastAPI endpoints for API integration
- [ ] RAG evaluation with RAGAS / TruLens
- [ ] Hallucination guardrails
- [ ] Version comparison with visual diffs
- [ ] Web UI (Streamlit or Next.js)
- [ ] PDF upload to S3 bucket

---

## 📌 Future Enhancements

- 🔐 Role-based access control (RBAC)
- 🧠 LLM voting / fallback logic for reliability
- 🌍 Multilingual PDF support
- 🧾 Structured output validation (Pydantic, JSONSchema)
- 📈 Streamlit Dashboard + Analytics
- ☁️ HuggingFace + Ollama + Bedrock integration

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch
3. Submit a PR with description, example use case, and tests

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Maintainer

**Bhagwat Chate**  
AI Architect | GenAI Expert | Multi-Agent RAG | AI System Design  
[🌐 GitHub](https://github.com/bhagwat-chate) · [💼 LinkedIn](https://www.linkedin.com/in/aimlbhagwatchate/)

---

> Built with ❤️ for scalable, compliance-aware document intelligence.