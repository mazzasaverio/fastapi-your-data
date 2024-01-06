# config.py
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    ENVIRONMENT = os.getenv("ENVIRONMENT")
    SQLALCHEMY_DATABASE_URL = (
        os.getenv("SQLALCHEMY_DATABASE_URL_DEV")
        if ENVIRONMENT == "development"
        else os.getenv("SQLALCHEMY_DATABASE_URL_PROD")
    )
    MONGODB_URL = (
        os.getenv("MONGODB_URL_DEV")
        if ENVIRONMENT == "development"
        else os.getenv("MONGODB_URL_PROD")
    )
    # Add configurations for other databases
