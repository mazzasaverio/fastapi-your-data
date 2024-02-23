from datetime import date
from pydantic import BaseModel
from typing import List, Optional


class UserBase(BaseModel):
    user_name: Optional[str] = None
    survey_id: Optional[str] = None
    survey_date: date
    survey_text: Optional[str] = None
    survey_embedding: Optional[List[float]] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    user_id: int

    class Config:
        from_attributes = True
