from datetime import date
from pydantic import BaseModel
from typing import List, Optional


class UserBase(BaseModel):
    user_name: str
    survey_id: int
    survey_date: date
    survey_text: str
    survey_embedding: Optional[List[float]] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True
