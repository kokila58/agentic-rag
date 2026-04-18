from typing import TypedDict, List, Generator
from langgraph.graph import StateGraph, END
from app.services.gemini_service import gemini_service
from app.tools.retrieval_tool import retrieve_documents
from app.memory.chat_memory import save_chat
# Agent State

class AgentState(TypedDict):

    question: str
    rewritten_question: str
    documents: List[str]
    answer: str
    session_id: str

# Query Rewrite Node

def rewrite_query(state: AgentState):

    question = state["question"]

    prompt = f"""
Rewrite the user question to improve document retrieval.

Question:
{question}

Improved Question:
"""

    improved_question = gemini_service.generate_response(prompt)

    return {
        "rewritten_question": improved_question.strip()
    }

# Retrieval Node

def retrieve(state: AgentState):

    question = state["rewritten_question"]

    docs = retrieve_documents(question)

    return {
        "documents": docs
    }

# Answer Generation Node

def generate_answer(state: AgentState):

    question = state["question"]
    docs = state["documents"]

    context = "\n\n".join(docs)

    prompt = f"""
You are an AI assistant answering questions from documents.

Use the provided context to answer accurately.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{question}

Answer:
"""

    answer = gemini_service.generate_response(prompt)

    return {
        "answer": answer
    }


# Memory Node

def store_memory(state: AgentState):

    question = state["question"]
    answer = state["answer"]
    session_id = state.get("session_id", "default")

    save_chat(session_id, question, answer)

    return {}


# Build Agent Graph
def build_agent():

    workflow = StateGraph(AgentState)

    workflow.add_node("rewrite", rewrite_query)
    workflow.add_node("retrieve", retrieve)
    workflow.add_node("generate", generate_answer)
    workflow.add_node("memory", store_memory)

    workflow.set_entry_point("rewrite")

    workflow.add_edge("rewrite", "retrieve")
    workflow.add_edge("retrieve", "generate")
    workflow.add_edge("generate", "memory")
    workflow.add_edge("memory", END)

    return workflow.compile()


rag_agent = build_agent()


# STREAMING FUNCTION

def stream_rag_answer(question: str, session_id: str) -> Generator[str, None, None]:

    # Step 1 → Run rewrite + retrieve
    result = rag_agent.invoke({
        "question": question,
        "session_id": session_id
    })

    docs = result["documents"]

    context = "\n\n".join(docs)

    prompt = f"""
You are an AI assistant answering questions from documents.

Use the provided context to answer accurately.

Context:
{context}

Question:
{question}

Answer:
"""

    full_answer = ""

    # STREAM tokens
    for token in gemini_service.stream_response(prompt):

        full_answer += token
        yield token

    # Save memory after streaming completes
    save_chat(session_id, question, full_answer)