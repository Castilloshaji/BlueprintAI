from uuid import UUID

from sqlalchemy.orm import Session

from app.models.project import Project
from app.models.user import User
from app.repositories.project_repository import project_repository
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectService:

    def create_project(
        self,
        db: Session,
        project_data: ProjectCreate,
        current_user: User,
    ) -> Project:

        project = Project(
            name=project_data.name,
            description=project_data.description,
            owner_id=current_user.id,
        )

        return project_repository.create(
            db,
            project,
        )

    def get_project(
        self,
        db: Session,
        project_id: UUID,
        current_user: User,
    ) -> Project:

        project = project_repository.get_by_id(
            db,
            project_id,
        )

        if not project:
            raise ValueError("Project not found")

        if project.owner_id != current_user.id:
            raise ValueError("Access denied")

        return project

    def get_projects(
        self,
        db: Session,
        current_user: User,
    ):

        return project_repository.get_by_owner(
            db,
            current_user.id,
        )

    def update_project(
        self,
        db: Session,
        project_id: UUID,
        project_data: ProjectUpdate,
        current_user: User,
    ):

        project = self.get_project(
            db,
            project_id,
            current_user,
        )

        update_data = project_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(project, key, value)

        return project_repository.update(
            db,
            project,
        )

    def delete_project(
        self,
        db: Session,
        project_id: UUID,
        current_user: User,
    ):

        project = self.get_project(
            db,
            project_id,
            current_user,
        )

        project_repository.delete(
            db,
            project,
        )


project_service = ProjectService()