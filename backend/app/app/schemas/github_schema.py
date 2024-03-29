from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserSchema(BaseModel):
    username: str
    location: Optional[str] = None
    updated_at: datetime

    class Config:
        from_attributes = True


# Pydantic does not directly support all SQLAlchemy types (like Vector), so for those, we'll need to use a workaround or simply represent them as a generic type (like str or a list of floats) depending on the expected data structure.
class RepositorySchema(BaseModel):
    repo_id: int
    repo_name: Optional[str] = None
    username: Optional[str] = None
    readme_raw: Optional[str] = None
    readme_cleaned: Optional[str] = None
    readme_embedding: Optional[List[float]] = None
    updated_at: datetime

    class Config:
        from_attributes = True
