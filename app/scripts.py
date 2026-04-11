from app.services.gemini_service import gemini_service
from app.services.embedding_service import embedding_service


print("Testing Gemini LLM...")

response = gemini_service.generate_response(
    "Explain what Retrieval Augmented Generation is in simple terms"
)

print(response)


print("\nTesting Embeddings...")

vector = embedding_service.generate_embedding("What is AI?")

print(len(vector))