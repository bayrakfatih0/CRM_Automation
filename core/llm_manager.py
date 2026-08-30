import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class LLMManager:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Gemini api key değişkeni bulunamadı...")

        genai.configure(api_key=api_key)

        self.model_name = "gemini-1.5-flash"

    def ask(self, prompt: str, system_context: str = "Sen bir yazılım test otomasyon uzmanısın. Yalnızca istenen bilgiyi kısa ve net ver.") -> str:
        try:
            model = genai.GenerativeModel(
                model_name = self.model_name,
                system_instruction = system_context
            )

            generation_config = genai.types.GenerationConfig(
                temperature = 0.1
            )

            response = model.generate_content(
                prompt,
                generation_config = generation_config
            )

            return response.text
        except Exception as e:
            return f"Gemini ile iletişimde bir hata oluştu: {str(e)}"