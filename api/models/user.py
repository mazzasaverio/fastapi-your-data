from sqlmodel import SQLModel, Field
import uuid


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str
    password: str
    token: str = Field(default_factory=lambda: str(uuid.uuid4()))

    class Config:
        schema_extra = {
            "example": {
                "email": "test@gmail.com",
                "username": "strong!!!",
                "events": [],
            }
        }
