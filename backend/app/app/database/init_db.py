# init_db.py
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from loguru import logger
from app.core.config import settings
from app.models.github_model import Base
from sqlalchemy.ext.asyncio.session import AsyncSession


def create_database(database_name, user, password, host, port):
    try:
        # Connect to the default database
        conn = psycopg2.connect(
            dbname=database_name, user=user, password=password, host=host, port=port
        )
        conn.autocommit = True
        cur = conn.cursor()

        # Check if database exists
        cur.execute(
            f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{database_name}'"
        )
        exists = cur.fetchone()
        if not exists:
            # Create database if it doesn't exist
            cur.execute(f"CREATE DATABASE {database_name}")
            logger.info(f"Database '{database_name}' created.")
        else:
            logger.info(f"Database '{database_name}' already exists.")

        # Close connection
        cur.close()
        conn.close()
    except Exception as e:
        logger.error(f"Error creating database: {e}")


from sqlalchemy import text


async def init_db() -> None:
    # def init_db():
    # Attempt to create the database if it doesn't exist

    create_database(
        settings.DB_NAME,
        settings.DB_USER,
        settings.DB_PASS,
        settings.DB_HOST,
        settings.DB_PORT,
    )

    # Create an engine instance
    engine = create_engine(settings.DATABASE_URI)

    # try:
    #     with engine.connect() as conn:
    #         conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
    # except Exception as e:
    #     logger.error(f"Error creating extension: {e}")

    # Create all tables in the database
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database initialized and all tables created")
    except OperationalError as e:
        logger.error(f"Error in initializing database: {e}")
