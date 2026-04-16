from app.services.embedding_service import embedding_service
from app.tools.hybrid_search_tool import hybrid_search
from app.tools.reranker_tool import rerank_documents


def retrieve_documents(query: str):

    # Convert question - embedding vector
    query_vector = embedding_service.create_embedding(query)

    # Hybrid retrieval
    documents = hybrid_search(query_vector, query)

    # rerank documents
    reranked_docs = rerank_documents(query, documents)

    return documents



    