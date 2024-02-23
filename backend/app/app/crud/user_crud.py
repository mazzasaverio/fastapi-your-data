# crud/user_crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.crud.base_crud import BaseCRUD

from app.models.user_model import UserSurveyModel


class UserSurveyCRUD(BaseCRUD):
    def __init__(self):
        super().__init__(model=UserSurveyModel)

    async def create_user_sarvey(
        self, db: AsyncSession, user_sarvey_data: dict
    ) -> UserSurveyModel:
        # Create new UserSurveyModel instance
        user_sarvey = UserSurveyModel(**user_sarvey_data)
        db.add(user_sarvey)
        await db.commit()
        await db.refresh(user_sarvey)
        return user_sarvey
