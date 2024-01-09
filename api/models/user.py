from sqlalchemy import Column, Integer, String
from api.database.connection import Base
from pydantic import BaseModel, EmailStr
import uuid


# SQLAlchemy model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    token = Column(String, default=lambda: str(uuid.uuid4()))


# Pydantic model
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    email: EmailStr
    token: str
