from uuid import UUID

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models.blueprint import Blueprint


class BlueprintRepository:

    def create(
        self,
        db: Session,
        blueprint: Blueprint,
    ) -> Blueprint:

        db.add(blueprint)
        db.commit()
        db.refresh(blueprint)

        return blueprint

    def get_by_id(
        self,
        db: Session,
        blueprint_id: UUID,
    ):

        return (
            db.query(Blueprint)
            .filter(Blueprint.id == blueprint_id)
            .first()
        )

    def get_by_project(
        self,
        db: Session,
        project_id: UUID,
    ):

        return (
            db.query(Blueprint)
            .filter(Blueprint.project_id == project_id)
            .all()
        )

    def update(
        self,
        db: Session,
        blueprint: Blueprint,
    ):

        db.commit()
        db.refresh(blueprint)

        return blueprint

    def delete(
        self,
        db: Session,
        blueprint: Blueprint,
    ):

        db.delete(blueprint)
        db.commit()
        
    def get_latest_version(
        self,
        db: Session,
        project_id: UUID,
    ) -> Blueprint | None:

        return (
            db.query(Blueprint) 
            .filter_by(project_id=project_id)
            .order_by(desc(Blueprint.version))
            .first()
        )    


blueprint_repository = BlueprintRepository()