from beanie import Document
from datetime import datetime
from typing import List, Dict


class DocsNameCateg(Document):
    id_file: str
    file_name: str
    url: str
    date_download: datetime
    date_extraction: datetime
    elements: List[Dict]

    class Settings:
        collection = "docs"
