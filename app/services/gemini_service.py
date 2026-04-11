import google.generativeai as genai
from app.config.settings import get_settings

settings = get_settings()

genai.configure(api_key=settings.GEMINI_API_KEY)


class GeminiService:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash-lite")

    def generate_response(self, prompt: str):

        response = self.model.generate_content(prompt)

        return response.text


gemini_service = GeminiService()