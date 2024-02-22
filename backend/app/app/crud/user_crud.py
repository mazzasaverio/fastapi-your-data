# crud/user_crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .base_crud import BaseCRUD
from app.models.user_model import UserModel
from app.schemas.user_schema import UserCreate


class UserCRUD(BaseCRUD[UserModel, UserCreate, UserCreate]):
    async def create_user(self, db: AsyncSession, *, obj_in: UserCreate) -> UserModel:
        db_obj = UserModel(
            user_name=obj_in.user_name,
            survey_id=obj_in.survey_id,
            survey_date=obj_in.survey_date,
            survey_text=obj_in.survey_text,
            survey_embedding=obj_in.survey_embedding,
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
