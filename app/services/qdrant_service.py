from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from app.config.settings import get_settings


settings = get_settings()

client = QdrantClient(
    url=settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY
)


def create_collection():

    collections = client.get_collections().collections
    collection_names = [c.name for c in collections]

    if settings.QDRANT_COLLECTION not in collection_names:

        client.create_collection(
            collection_name=settings.QDRANT_COLLECTION,
            vectors_config=VectorParams(
                size=768,
                distance=Distance.COSINE
            )
        )

def store_embeddings(vectors, payloads):

    points = []

    for i, vector in enumerate(vectors):

        points.append(
            PointStruct(
                id=i,
                vector=vector,
                payload=payloads[i]
            )
        )

    client.upsert(
        collection_name=settings.QDRANT_COLLECTION,
        points=points
    )

def search_vectors(query_vector, limit=5):

    results = client.search(
        collection_name=settings.QDRANT_COLLECTION,
        query_vector=query_vector,
        limit=limit
    )

    documents = []

    for result in results:
        documents.append(result.payload["text"])

    return documents