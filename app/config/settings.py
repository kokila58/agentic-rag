from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):

    # App
    APP_ENV: str = "development"
    LOG_LEVEL: str = "INFO"

    # Gemini
    GEMINI_API_KEY: str

    # Qdrant
    QDRANT_URL: str
    QDRANT_API_KEY: str
    QDRANT_COLLECTION: str = "agentic_rag_docs"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings():
    return Settings()