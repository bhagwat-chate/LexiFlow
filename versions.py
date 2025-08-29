import importlib.metadata
packages = [
    "aiohttp",
    "docx2txt",
    "faiss-cpu",
    "google-ai-generativelanguage",
    "groq",
    "langchain",
    "langchain-community",
    "langchain-core",
    "langchain-google-genai",
    "langchain-groq",
    "langchain-openai",
    "langchain-text-splitters",
    "langsmith",
    "numpy",
    "openai",
    "pandas",
    "pydantic",
    "pydantic-settings",
    "PyMuPDF",
    "pypdf",
    "python-dotenv",
    "SQLAlchemy",
    "structlog",
    "tiktoken"
]

for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")

# # serve static & templates
# app.mount("/static", StaticFiles(directory="../static"), name="static")
# templates = Jinja2Templates(directory="../templates")
