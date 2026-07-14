from app.ai.prompts.blueprint_prompt import BLUEPRINT_SYSTEM_PROMPT


class PromptBuilder:

    @staticmethod
    def build_blueprint_prompt(
        user_prompt: str,
    ):

        return [
            {
                "role": "system",
                "content": BLUEPRINT_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ]


prompt_builder = PromptBuilder()