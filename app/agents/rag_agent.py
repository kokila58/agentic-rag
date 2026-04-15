from typing import TypedDict, List
from langgraph.graph import StateGraph, END

from app.services.gemini_service import gemini_service
from app.tools.retrieval_tool import retrieve_documents



class AgentState(TypedDict):

    question: str
    documents: List[str]
    answer: str


def retrieve(state: AgentState):

    question = state["question"]

    docs = retrieve_documents(question)

    return {
        "documents": docs
    }


def generate_answer(state: AgentState):

    question = state["question"]
    docs = state["documents"]

    context = "\n".join(docs)

    prompt = f"""
    Answer the question using the provided context.

    Context:
    {context}

    Question:
    {question}
    """

    answer = gemini_service.generate_response(prompt)

    return {
        "answer": answer
    }


def build_agent():

    workflow = StateGraph(AgentState)

    workflow.add_node("retrieve", retrieve)
    workflow.add_node("generate", generate_answer)

    workflow.set_entry_point("retrieve")

    workflow.add_edge("retrieve", "generate")

    workflow.add_edge("generate", END)

    return workflow.compile()

rag_agent = build_agent()