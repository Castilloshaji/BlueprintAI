from sqlalchemy.orm import Session

from app.ai.generators.blueprint_generator import blueprint_generator
from app.models.blueprint import Blueprint
from app.repositories.blueprint_repository import blueprint_repository


class BlueprintService:

    def generate(
        self,
        db: Session,
        project_id,
        prompt: str,
    ):

        latest = blueprint_repository.get_latest_version(
            db,
            project_id,
        )

        version = 1

        if latest:
            version = latest.version + 1

        blueprint = blueprint_generator.generate(
            prompt
        )

        entity = Blueprint(

            project_id=project_id,

            version=version,

            prompt=prompt,

            architecture=blueprint.architecture,

            database_schema=blueprint.database_schema,

            api_design=blueprint.api_design,

            folder_structure=blueprint.folder_structure,

            roadmap=blueprint.roadmap,

        )

        return blueprint_repository.create(
            db,
            entity,
        )


blueprint_service = BlueprintService()