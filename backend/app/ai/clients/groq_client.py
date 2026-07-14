from groq import Groq

from app.core.config import settings


class GroqClient:

    def __init__(self):
        self.client = Groq(
            api_key=settings.groq_api_key,
        )

    def chat(
        self,
        messages,
        model="llama-3.3-70b-versatile",
        temperature=0.1,
    ):

        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            response_format={
                "type": "json_object"
            },
        )

        return response.choices[0].message.content


groq_client = GroqClient()