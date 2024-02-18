import os
from dotenv import load_dotenv
from loguru import logger
import sys
from pathlib import Path

# Dynamically obtain the path to the 'backend' directory
backend_dir_path = Path(__file__).parents[3]

# Construct the path to the .env file located in the project root
dotenv_path = backend_dir_path.parent / ".env"

# Load the .env file
load_dotenv(dotenv_path=dotenv_path)


class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", 5432))
    DB_NAME = os.getenv("DB_NAME", "postgres")
    DB_PASS = os.getenv("DB_PASS", "postgres")
    DB_USER = os.getenv("DB_USER", "postgres")
    GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
    DATABASE_URI: str = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    LOCATION = os.getenv("LOCATION", "Milan")
    MAX_USERS = int(os.getenv("MAX_USERS", 10))
    MAX_REPOS_PER_USER = int(os.getenv("MAX_REPOS_PER_USER", 5))


class LogConfig:
    LOGGING_LEVEL = "DEBUG"
    LOGGING_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

    @staticmethod
    def configure_logging():
        logger.remove()

        logger.add(
            sys.stderr, format=LogConfig.LOGGING_FORMAT, level=LogConfig.LOGGING_LEVEL
        )
        # Create logs directory if it doesn't exist
        # logs_dir = backend_dir_path / "github_data/logs"
        # logs_dir.mkdir(parents=True, exist_ok=True)
        # logger.add(
        #     logs_dir / "runtime_{time}.log",
        #     rotation="10 MB",
        #     level=LogConfig.LOGGING_LEVEL,
        # )


# Call the configure method to setup logging as per the configuration
LogConfig.configure_logging()
