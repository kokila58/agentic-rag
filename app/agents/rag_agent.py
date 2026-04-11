from typing import TypedDict, List
from langgraph.graph import StateGraph, END

from app.services.gemini_service import gemini_service
# from app.tools.retrieval_tool import retrieve_documents



class AgentState(TypedDict):

    question: str
    documents: List[str]
    answer: str