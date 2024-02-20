from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class DocumentsResponse(BaseModel):
    id: int
    url: str
    status: str
    notes: Optional[str]
    download_path: str
    downloaded_at: datetime
    keywords_namefile: str
