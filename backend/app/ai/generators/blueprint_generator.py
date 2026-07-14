from app.ai.prompts.prompt_builder import prompt_builder
from app.ai.services.llm_service import llm_service
from app.ai.parsers.response_parser import response_parser


class BlueprintGenerator:

    def generate(
        self,
        prompt: str,
    ):

        messages = prompt_builder.build_blueprint_prompt(
            prompt
        )

        response = llm_service.generate(
            messages
        )
        with open("groq_response.txt", "w", encoding="utf-8") as f:
            f.write(response)

        print("\n========== RAW AI RESPONSE ==========\n")
        print("=" * 100)
        print(response)
        print("=" * 100)
        print("\n=====================================\n")

        blueprint = response_parser.parse(
            response
        )

        return blueprint


blueprint_generator = BlueprintGenerator()