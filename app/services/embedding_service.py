from google import genai
from app.config.settings import get_settings

settings = get_settings()

client = genai.Client(api_key=settings.GEMINI_API_KEY)


class EmbeddingService:

    def create_embedding(self, text: str):

        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=text
        )

        return response.embeddings[0].values


embedding_service = EmbeddingService()