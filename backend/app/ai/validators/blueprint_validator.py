REQUIRED_FIELDS = [
    "title",
    "architecture",
    "database_schema",
    "api_design",
    "folder_structure",
    "roadmap",
]


class BlueprintValidator:

    @staticmethod
    def validate(data: dict):

        missing = []

        for field in REQUIRED_FIELDS:

            if field not in data:
                missing.append(field)

        if missing:
            raise ValueError(
                f"Missing fields: {', '.join(missing)}"
            )

        if not isinstance(data["title"], str):
            raise ValueError("title must be a string.")

        OBJECT_FIELDS = [
            "architecture",
            "database_schema",
            "api_design",
            "folder_structure",
            "roadmap",
        ]

        for field in OBJECT_FIELDS:

            if not isinstance(data[field], dict):
                raise ValueError(
                    f"{field} must be a JSON object."
                )

        return True


blueprint_validator = BlueprintValidator()