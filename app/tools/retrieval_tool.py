from app.services.embedding_service import embedding_service
from app.services.qdrant_service import search_vectors

def retrieve_documents(query: str):

    # convert query → embedding
    query_vector = embedding_service.create_embedding(query)

    # search vector database
    documents = search_vectors(query_vector)

    return documents