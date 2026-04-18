from google import genai
from app.config.settings import get_settings

settings = get_settings()

class GeminiService:

    def __init__(self):

        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    def generate_response(self, prompt: str):

        response = self.client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text

    # STREAMING METHOD
    def stream_response(self, prompt: str):

        stream = self.client.models.generate_content_stream(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        for chunk in stream:
            if chunk.text:
                yield chunk.text


gemini_service = GeminiService()