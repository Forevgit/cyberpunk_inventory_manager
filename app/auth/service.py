from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from auth import models, schemas
from auth.password_service import PasswordService
from auth.token_service import TokenService
from typing import Optional
from sqlalchemy import or_

class AuthService:
    def __init__(self, db: AsyncSession, password_service: PasswordService, token_service: TokenService):
        self.db: AsyncSession = db
        self.password_service: PasswordService = password_service
        self.token_service: TokenService = token_service

    async def create_user(self, user_data: schemas.UserCreate) -> Optional[models.User]:
        existing_user: Optional[models.User] = await self.db.scalar(
            select(models.User).filter(
                or_(
                    models.User.username == user_data.username,
                    models.User.email == user_data.email
                )
            )
        )
        if existing_user:
            return None

        hashed_password = self.password_service.get_password_hash(user_data.password)
        user = models.User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hashed_password
        )
        try:
            self.db.add(user)
            await self.db.commit()
            await self.db.refresh(user)
            return user
        except IntegrityError:
            await self.db.rollback()
            return None

    async def authenticate_user(self, username: str, password: str) -> Optional[models.User]:
        result = await self.db.execute(select(models.User).filter(models.User.username == username))
        user: Optional[models.User] = result.scalars().first()
        if not user or not self.password_service.verify_password(password, user.hashed_password):
            return None
        return user
