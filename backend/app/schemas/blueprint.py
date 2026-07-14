from uuid import UUID
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class BlueprintCreate(BaseModel):
    project_id: UUID
    prompt: str


class BlueprintGenerate(BaseModel):
    prompt: str


class BlueprintResponse(BaseModel):
    id: UUID
    project_id: UUID

    version: int

    prompt: str

    architecture: dict[str, Any] | None = None
    database_schema: dict[str, Any] | None = None
    api_design: dict[str, Any] | None = None
    folder_structure: dict[str, Any] | None = None
    roadmap: dict[str, Any] | None = None

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )


class BlueprintUpdate(BaseModel):
    architecture: dict[str, Any] | None = None
    database_schema: dict[str, Any] | None = None
    api_design: dict[str, Any] | None = None
    folder_structure: dict[str, Any] | None = None
    roadmap: dict[str, Any] | None = None