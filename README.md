# 🤖 Agentic RAG Document Assistant | FastAPI, LangGraph, Qdrant, Gemini

An **Agentic Retrieval-Augmented Generation (RAG)** system that enables users to interact with documents using natural language.

This system goes beyond traditional RAG by incorporating **LangGraph-based AI agents**, enabling **multi-step reasoning, hybrid retrieval, and contextual memory** for more accurate and intelligent responses.



## 🚀 Why This Project Matters

Most RAG systems follow a static pipeline:

> Retrieve → Generate

This project implements an **Agentic RAG architecture**:

> Reason → Rewrite → Retrieve → Rerank → Generate → Remember

✅ Improves retrieval accuracy
✅ Enables context-aware conversations
✅ Mimics real-world AI assistant behavior



## ✨ Core Features 

### 📁 Document Management

*  Upload PDF documents via API
*  List all uploaded documents
*  Delete documents

### 🔍 Advanced Retrieval System

*  Semantic Search (embedding-based)
*  Keyword Search (text-based)
*  Hybrid Search (semantic + keyword)
*  Reranking for relevance optimization

### 💾 Document Processing Pipeline

*  PDF parsing using PyPDF
*  Smart chunking for contextual segmentation
*  Embedding generation (Google Gemini)
*  Vector storage using Qdrant

### 🤖 Agentic Intelligence Layer

*  LangGraph-based agent workflow
*  Query rewriting for better retrieval
*  Multi-step reasoning pipeline
*  Context-aware response generation

### 🧠 Memory System

*  Persistent chat memory per session
*  Context retention for follow-up queries

### ⚡ Backend & API

*  RESTful API using FastAPI
*  Streaming-ready architecture
*  Configurable environment setup



## 🏗️ System Architecture


                ┌───────────────┐
                │     USER      │
                └──────┬────────┘
                       ↓
                ┌───────────────┐
                │   FastAPI API │
                └──────┬────────┘
                       ↓
               ┌──────────────────┐
               │ LangGraph Agent  │
               └──────┬───────────┘
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
 Query Rewrite   Retrieval Tool   Memory
        ↓             ↓             ↓
        └──────→ Context Builder ←─┘
                       ↓
                ┌───────────────┐
                │ Gemini LLM    │
                └──────┬────────┘
                       ↓
                ┌───────────────┐
                │   Response    │
                └───────────────┘




## 🔧 Tech Stack

| Layer            | Technology        |
| ---------------- | ----------------- |
| Backend          | FastAPI           |
| Agent Framework  | LangGraph         |
| LLM              | Google Gemini     |
| Embeddings       | Gemini Embeddings |
| Vector DB        | Qdrant            |
| Document Parsing | PyPDF             |
| Memory           | Custom JSON-based |
| Config           | Pydantic          |



## ⚙️ How It Works

### 📌 Document Ingestion

1. Upload PDF
2. Extract text
3. Chunk into segments
4. Generate embeddings
5. Store in Qdrant

### 📌 Query Processing

1. User sends query
2. Agent rewrites query
3. Hybrid retrieval executes
4. Results are reranked
5. Context is constructed
6. Gemini generates answer
7. Memory is updated



## 📊 Evaluation & Metrics (Important for Interviews)

This system can be evaluated using:

| Metric              | Description                         |
| ------------------- | ----------------------------------- |
| Retrieval Accuracy  | Top-K relevance of retrieved chunks |
| Answer Quality      | LLM response correctness            |
| Latency             | End-to-end response time            |
| Context Utilization | Relevance of used chunks            |

### Suggested Improvements

* Integrate Langfuse / LangSmith for tracing
* Add automated evaluation pipeline
* Benchmark hybrid vs semantic search



## 📂 Project Structure


app/
 ├── api/
 ├── agents/
 ├── services/
 ├── ingestion/
 ├── tools/
 ├── memory/
 └── config/

storage/
uploaded_docs/


---

##  API Usage

### Upload Document

```
POST /documents/upload
```

### Chat

```
POST /chat/
```

### List Documents

```
GET /documents/
```

### Delete Document

```
DELETE /documents/{id}


