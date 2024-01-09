from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "test@gmail.com",
                "username": "strong!!!",
                "events": [],
            }
        }
