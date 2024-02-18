from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    location = Column(String)
    updated_at = Column(DateTime, default=datetime.utcnow)


class Repository(Base):
    __tablename__ = "repositories"
    repo_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    username = Column(String)
    name = Column(String, nullable=False)
    readme_raw = Column(String)
    readme_cleaned = Column(String)
    readme_embedding = Column(Vector)
    updated_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="repositories")


User.repositories = relationship(
    "Repository", order_by=Repository.repo_id, back_populates="user"
)
