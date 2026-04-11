from fastapi import FastAPI
from app.config.settings import get_settings

from app.services.qdrant_service import create_collection

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


@app.on_event("startup")
def startup():

    create_collection()