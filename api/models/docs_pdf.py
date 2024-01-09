from sqlmodel import SQLModel, Field
from datetime import datetime


class PdfDownload(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    url: str = Field(sa_column_kwargs={"unique": True})
    status: str
    notes: str
    download_path: str
    downloaded_at: datetime = Field(default_factory=datetime.utcnow)
    keywords_namefile: str
