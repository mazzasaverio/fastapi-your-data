from sqlalchemy import Column, Integer, String, DateTime
from app.app.database.session import Base
from datetime import datetime


class Documents(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True)
    status = Column(String)
    notes = Column(String)
    download_path = Column(String)
    downloaded_at = Column(DateTime, default=datetime.utcnow)
    keywords_namefile = Column(String)
