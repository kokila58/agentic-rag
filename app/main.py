from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import get_settings
from app.api.document_api import router as document_router
from app.api.chat_api import router as chat_router
from app.services.qdrant_service import create_collection


settings = get_settings()




app = FastAPI(
    title="Agentic RAG Document Assistant",
    version="1.0.0",
    description="Production-ready Agentic RAG system using Gemini, LangGraph, and Qdrant"
)


# CORS middleware (useful for frontend integration later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Startup event
@app.on_event("startup")
def startup_event():
    print("Starting Agentic RAG API...")
    create_collection()


# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Agentic RAG API running",
        "environment": settings.APP_ENV
    }


# Register routers
app.include_router(document_router)
app.include_router(chat_router)