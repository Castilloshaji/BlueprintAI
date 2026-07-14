from uuid import UUID

from sqlalchemy.orm import Session

from app.models.project import Project


class ProjectRepository:

    def create(
        self,
        db: Session,
        project: Project,
    ) -> Project:

        db.add(project)
        db.commit()
        db.refresh(project)

        return project

    def get_by_id(
        self,
        db: Session,
        project_id: UUID,
    ) -> Project | None:

        return (
            db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

    def get_by_owner(
        self,
        db: Session,
        owner_id: UUID,
    ) -> list[Project]:

        return (
            db.query(Project)
            .filter(Project.owner_id == owner_id)
            .all()
        )

    def update(
        self,
        db: Session,
        project: Project,
    ) -> Project:

        db.commit()
        db.refresh(project)

        return project

    def delete(
        self,
        db: Session,
        project: Project,
    ):

        db.delete(project)
        db.commit()

    def get_by_id_and_owner(
        self,
        db: Session,
        project_id: UUID,
        owner_id: UUID,
    ) -> Project | None:

        return (
            db.query(Project)
            .filter_by(
            id=project_id,
            owner_id=owner_id,
        )
        .first()
    )

project_repository = ProjectRepository()