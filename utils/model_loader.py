import os
import sys
from dotenv import load_dotenv
from utils.config_loader import load_config
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException

load_dotenv()
log = CustomLogger().get_logger(__name__)


class ModelLoader:
    """
    ModelLoader is responsible for initializing and loading both embedding models and
    large language models (LLMs) based on environment variables and YAML configuration.

    This loader supports multiple providers including OpenAI, Google, and Groq,
    and is designed for modular, plug-and-play use in Retrieval-Augmented Generation (RAG)
    systems and GenAI pipelines.

    Environment Variables:
        - EMBEDDING_PROVIDER: str, default='openai'
        - LLM_PROVIDER: str, default='openai'
        - OPENAI_API_KEY, GOOGLE_API_KEY, GROQ_API_KEY

    Config Structure (YAML):
        - embedding_model: {openai: {model_name: ...}, google: {...}}
        - llm: {openai: {...}, google: {...}, groq: {...}}

    Raises:
        DocumentPortalException: If required environment variables are missing or
                                 unsupported providers are configured.
    """

    def __init__(self):
        """
        Initializes the ModelLoader by validating environment variables and loading configuration.

        Raises:
            DocumentPortalException: If any required API keys are missing or invalid.
        """
        self._validate_env_var()
        self.config = load_config()
        log.info("configuration load successful", config_keys=list(self.config.keys()))

    def _validate_env_var(self):
        """
        Validates the presence of required environment variables for API keys.

        Expected variables:
            - OPENAI_API_KEY
            - GOOGLE_API_KEY
            - GROQ_API_KEY

        Raises:
            DocumentPortalException: If any of the required keys are missing.
        """
        required_keys = ['GROQ_API_KEY', 'GOOGLE_API_KEY', 'OPENAI_API_KEY']
        self.api_keys = {key: os.getenv(key) for key in required_keys}
        missing_keys = {k for k, v in self.api_keys.items() if not v}

        if missing_keys:
            log.error(f"missing environment variable(s): {missing_keys}")
            raise DocumentPortalException("Missing environment variables.", sys)

        log.info(f"environment variables validated: {list(self.api_keys.keys())}")

    def load_embedding(self):
        """
        Loads the embedding model specified via the EMBEDDING_PROVIDER environment variable
        and YAML configuration. Supports 'openai' and 'google'.

        Returns:
            BaseEmbedding: An instance of the selected embedding model.

        Raises:
            DocumentPortalException: If provider is unsupported or model loading fails.
        """
        try:
            log.info("loading embedding model...")

            provider_key = os.getenv("EMBEDDING_PROVIDER", "openai").lower()
            embedding_config = self.config['embedding_model'].get(provider_key)

            if not embedding_config:
                raise DocumentPortalException(f"Unsupported embedding provider: '{provider_key}'")

            model_name = embedding_config.get('model_name')

            if provider_key == 'openai':
                embedding_model = OpenAIEmbeddings(model=model_name)
            elif provider_key == 'google':
                embedding_model = GoogleGenerativeAIEmbeddings(model=model_name)
            else:
                raise DocumentPortalException(f"Embedding provider '{provider_key}' is not implemented.")

            log.info("embedding model loaded successfully.", provider=provider_key, model=model_name)
            return embedding_model

        except Exception as e:
            log.error(f"error in embedding load: {str(e)}")
            raise DocumentPortalException("Error loading embedding model", e)

    def load_model(self):
        """
        Loads the LLM specified via the LLM_PROVIDER environment variable
        and YAML configuration. Supports 'openai', 'google', and 'groq'.

        Returns:
            BaseLLM: An instance of the selected LLM for text generation.

        Raises:
            DocumentPortalException: If provider is unsupported or model loading fails.
        """
        try:
            log.info("loading the LLM...")

            provider_key = os.getenv("LLM_PROVIDER", "openai")
            if provider_key not in self.config["llm"]:
                raise DocumentPortalException(f"Unsupported LLM provider: {provider_key}")

            llm_block = self.config['llm'][provider_key]
            model_name = llm_block.get('model_name')
            temperature = llm_block.get('temperature', 0.0)
            max_output_tokens = llm_block.get('max_output_tokens', 2048)

            if provider_key == 'openai':
                model = ChatOpenAI(model=model_name, temperature=temperature,
                                   max_tokens=max_output_tokens, timeout=None, max_retries=2)
            elif provider_key == 'google':
                model = ChatGoogleGenerativeAI(model=model_name, temperature=temperature,
                                   max_tokens=max_output_tokens, timeout=None, max_retries=2)
            elif provider_key == 'groq':
                model = ChatGroq(model=model_name, temperature=temperature,
                                   max_tokens=max_output_tokens, timeout=None, max_retries=2)
            else:
                raise DocumentPortalException(f"LLM provider '{provider_key}' is not supported.")

            log.info("LLM loaded successfully", provider=provider_key, model=model_name)
            return model

        except Exception as e:
            log.error(f"error in LLM load: {str(e)}")
            raise DocumentPortalException("Error loading LLM model", e)

    def load_llm(self):
        return self.load_model()
