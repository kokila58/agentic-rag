from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import uuid

from app.config.settings import get_settings

settings = get_settings()

# Initialize Qdrant Client
client = QdrantClient(
    url=settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY,
    timeout=60,                # prevent timeout
    check_compatibility=False  # avoid compatibility warning
)

BATCH_SIZE = 20


# Create collection
def create_collection():

    collections = client.get_collections().collections
    collection_names = [c.name for c in collections]

    if settings.QDRANT_COLLECTION not in collection_names:

        client.create_collection(
            collection_name=settings.QDRANT_COLLECTION,
            vectors_config=VectorParams(
                size=3072,   # FIXED
                distance=Distance.COSINE
            )
        )

        print(f"Collection {settings.QDRANT_COLLECTION} created")

    else:
        print(f"Collection {settings.QDRANT_COLLECTION} already exists")

# Store embeddings (Batch Upload Fix)
def store_embeddings(vectors, payloads):

    points = []

    for i, vector in enumerate(vectors):

        point = PointStruct(
            id=str(uuid.uuid4()),   # unique ID
            vector=vector,
            payload=payloads[i]
        )

        points.append(point)

    # Upload in batches
    for i in range(0, len(points), BATCH_SIZE):

        batch = points[i:i + BATCH_SIZE]

        client.upsert(
            collection_name=settings.QDRANT_COLLECTION,
            points=batch
        )


# Search vectors
def search_vectors(query_vector, limit=5):

    results = client.query_points(
        collection_name=settings.QDRANT_COLLECTION,
        query=query_vector,
        limit=limit
    )

    documents = []

    for point in results.points:

        payload = point.payload

        if payload and "text" in payload:
            documents.append(payload["text"])

    return documents


# Delete document vectors
def delete_document_vectors(source_file):

    client.delete(
        collection_name=settings.QDRANT_COLLECTION,
        points_selector={
            "filter": {
                "must": [
                    {
                        "key": "source",
                        "match": {
                            "value": source_file
                        }
                    }
                ]
            }
        }
    )