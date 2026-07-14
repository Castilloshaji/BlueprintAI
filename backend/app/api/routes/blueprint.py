from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.blueprint import (
    BlueprintGenerate,
    BlueprintResponse,
)
from app.services.blueprint_service import blueprint_service
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/blueprints",
    tags=["Blueprints"],
)
@router.post(
    "/generate",
    response_model=BlueprintResponse,
)
def generate_blueprint(
    project_id: str,
    request: BlueprintGenerate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:

        return blueprint_service.generate(
            db=db,
            project_id=project_id,
            prompt=request.prompt,
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.security import get_current_user

from app.models.user import User

from app.repositories.project_repository import project_repository
from app.schemas.blueprint import (
    BlueprintGenerate,
    BlueprintResponse,
)

from app.services.blueprint_service import blueprint_service


router = APIRouter(
    tags=["Blueprints"],
)        
@router.post(
    "/projects/{project_id}/blueprints",
    response_model=BlueprintResponse,
    status_code=status.HTTP_201_CREATED,
)
def generate_blueprint(
    project_id: UUID,
    request: BlueprintGenerate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    project = project_repository.get_by_id_and_owner(
        db=db,
        project_id=project_id,
        owner_id=current_user.id,
    )

    if project is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )

    return blueprint_service.generate(
        db=db,
        project_id=project.id,
        prompt=request.prompt,
    )