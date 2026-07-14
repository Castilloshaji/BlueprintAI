from dataclasses import dataclass
from typing import Any


@dataclass
class BlueprintDTO:

    title: str

    architecture: dict[str, Any]

    database_schema: dict[str, Any]

    api_design: dict[str, Any]

    folder_structure: dict[str, Any]

    roadmap: dict[str, Any]