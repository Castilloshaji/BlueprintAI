from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from app.models.user import User
from app.repositories.user_repository import user_repository
from app.schemas.user import UserCreate


class AuthService:

    def register(
        self,
        db: Session,
        user_data: UserCreate,
    ) -> User:

        if user_repository.get_by_email(
            db,
            user_data.email,
        ):
            raise ValueError("Email already registered")

        if user_repository.get_by_username(
            db,
            user_data.username,
        ):
            raise ValueError("Username already exists")

        user = User(
            username=user_data.username,
            email=user_data.email,
            password_hash=hash_password(user_data.password),
            full_name=user_data.full_name,
        )

        return user_repository.create(
            db,
            user,
        )

    def login(
        self,
        db: Session,
        email: str,
        password: str,
    ):

        user = user_repository.get_by_email(
            db,
            email,
        )

        if not user:
            raise ValueError("Invalid email or password")

        if not verify_password(
            password,
            user.password_hash,
        ):
            raise ValueError("Invalid email or password")

        token = create_access_token(
            {
                "sub": user.email
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }


auth_service = AuthService()