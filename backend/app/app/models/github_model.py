from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from datetime import datetime

Base = declarative_base()


class GitUser(Base):
    __tablename__ = "git_users_n"
    username = Column(String, primary_key=True)
    location = Column(String)
    updated_at = Column(DateTime, default=datetime.utcnow)


class GitRepository(Base):
    __tablename__ = "git_repositories_n"
    repo_id = Column(Integer, primary_key=True)
    repo_name = Column(String)
    username = Column(String, ForeignKey("git_users_n.username"))
    readme_raw = Column(String)
    readme_cleaned = Column(String)
    readme_embedding = Column(Vector)
    updated_at = Column(DateTime, default=datetime.utcnow)
