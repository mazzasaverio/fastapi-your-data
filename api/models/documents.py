from sqlalchemy import Column, Integer, String, DateTime
from api.database.connection import Base
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# SQLAlchemy ORM model
class Documents(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True)
    status = Column(String)
    notes = Column(String)
    download_path = Column(String)
    downloaded_at = Column(DateTime, default=datetime.utcnow)
    keywords_namefile = Column(String)


# Pydantic model for request/response validation


class DocumentsResponse(BaseModel):
    id: int
    url: str
    status: str
    notes: Optional[str]  # Allow None values
    download_path: str
    downloaded_at: datetime
    keywords_namefile: str
