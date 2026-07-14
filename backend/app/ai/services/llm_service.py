from app.ai.clients.groq_client import groq_client


class LLMService:

    def generate(
        self,
        messages,
    ):

        return groq_client.chat(
            messages=messages,
        )


llm_service = LLMService()