import google.generativeai as genai
from app.config.settings import get_settings

settings = get_settings()

genai.configure(api_key=settings.GEMINI_API_KEY)


class EmbeddingService:

    def generate_embedding(self, text: str):

        result = genai.embed_content(
            model="gemini-embedding-001",
            content=text
        )

        return result["embedding"]


embedding_service = EmbeddingService()