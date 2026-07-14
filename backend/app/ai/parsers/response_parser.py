import json

from app.ai.validators.blueprint_validator import blueprint_validator
from app.dto.blueprint_dto import BlueprintDTO


class ResponseParser:

    @staticmethod
    def parse(response: str) -> BlueprintDTO:

        response = response.strip()

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end ==-1:
            raise ValueError("No JSON object found in AI response.")

        response = response[start:end + 1]

        try:
            data = json.loads(response)

        except json.JSONDecodeError as e:

            raise ValueError(
                f"""
AI returned invalid JSON.

JSON Error:
{e}

Response:

{response}
"""
            )

        blueprint_validator.validate(data)

        return BlueprintDTO(
            title=data["title"],
            architecture=data["architecture"],
            database_schema=data["database_schema"],
            api_design=data["api_design"],
            folder_structure=data["folder_structure"],
            roadmap=data["roadmap"],
        )


response_parser = ResponseParser()