from fastapi import APIRouter
from sqlalchemy import text

from app.database.database import SessionLocal

router = APIRouter()


@router.get("/database", tags=["Database"])
def database_check():
    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "Connected",
            "database": "PostgreSQL",
        }
    finally:
        db.close()