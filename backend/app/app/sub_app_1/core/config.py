import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from typing import List
import json
from loguru import logger
import sys

load_dotenv()


class Settings(BaseSettings):
    # API_VERSION: str = "v1"
    # API_V1_STR: str = f"/api/{API_VERSION}"

    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_PASS: str = os.getenv("DB_PASS")
    DB_USER: str = os.getenv("DB_USER")

    DATABASE_URI: str = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    ASYNC_DATABASE_URI: str = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # github module settings
    GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")

    LOCATION = os.getenv("LOCATION", "Milan")
    MAX_USERS = int(os.getenv("MAX_USERS", 10))
    MAX_REPOS_PER_USER = int(os.getenv("MAX_REPOS_PER_USER", 5))


settings = Settings()
