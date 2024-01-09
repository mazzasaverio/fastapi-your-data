from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class PdfDownload(Base):
    __tablename__ = "pdf_downloads"
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    status = Column(String)  # 'success', 'failed', etc.
    notes = Column(String)  # Additional information like error messages
    download_path = Column(String)
    downloaded_at = Column(DateTime, default=datetime.utcnow)
    keywords_namefile = Column(String)  # Nuova colonna per le parole chiave

    def __repr__(self):
        return f"<PdfDownload(url='{self.url}', status='{self.status}', downloaded_at='{self.downloaded_at}', keywords_namefile='{self.keywords_namefile}')>"
