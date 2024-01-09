# app/config/settings.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    environment: str = "development"
    sqlalchemy_database_url: str
    mongodb_url: str
    api_key: str  # Add the API key variable

    class Config:
        env_file = ".env"


settings = Settings()
