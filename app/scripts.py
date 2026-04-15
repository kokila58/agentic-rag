# from app.services.gemini_service import gemini_service
# from app.services.embedding_service import embedding_service


# print("Testing Gemini LLM...")

# response = gemini_service.generate_response(
#     "Explain what Retrieval Augmented Generation is in simple terms"
# )

# print(response)


# print("\nTesting Embeddings...")

# vector = embedding_service.generate_embedding("What is AI?")

# print(len(vector))


from qdrant_client import QdrantClient

client = QdrantClient(
    url="https://5b231b72-0915-4cbe-8146-fee6ab179f20.us-west-2-0.aws.cloud.qdrant.io",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwic3ViamVjdCI6ImFwaS1rZXk6NTFkYjI0MWYtZmExMy00ZGFiLWE0NzMtNzk0Yzk0YTljNzY4In0.Flc3jycXB8gkx9WPBGB5X4WgjHtWNISioxcff-kQTQI"
)

print(client.get_collections())


client.delete_collection("agentic_rag_docs")