from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.agents.rag_agent import rag_agent, stream_rag_answer


class ChatRequest(BaseModel):

    question: str
    session_id: str


router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/")
def chat_with_documents(request: ChatRequest):

    result = rag_agent.invoke({
        "question": request.question,
        "session_id": request.session_id
    })

    return {
        "question": request.question,
        "answer": result["answer"]
    }


# STREAMING CHAT

@router.post("/stream")
def chat_stream(request: ChatRequest):

    def generate():

        for token in stream_rag_answer(
            request.question,
            request.session_id
        ):
            yield token

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )