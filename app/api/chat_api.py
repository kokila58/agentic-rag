from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.rag_agent import rag_agent

class ChatRequest(BaseModel):
    question: str


router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/")
def chat_with_documents(request: ChatRequest):

    result = rag_agent.invoke({
        "question": request.question
    })

    return {
        "question": request.question,
        "answer": result["answer"]
    }