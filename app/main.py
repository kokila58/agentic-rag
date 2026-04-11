from fastapi import FastAPI
from app.config.settings import get_settings

settings = get_settings()

app = FastAPI(
    title="Agentic RAG Document Assistant",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Agentic RAG API running"
    }