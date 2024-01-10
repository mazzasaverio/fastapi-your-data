from sqlalchemy import Column, Integer, String
from app.database.sqlalchemy_connection import Base
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    token = Column(String, default=lambda: str(uuid.uuid4()))
