# init_db.py
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from loguru import logger
from app.core.config import settings
from app.models.github_model import Base
from app.models.user_model import Base


from sqlalchemy.ext.asyncio.session import AsyncSession
import asyncpg
from sqlalchemy.ext.asyncio import create_async_engine


async def create_extension():
    conn: asyncpg.Connection = await asyncpg.connect(
        user=settings.DB_USER,
        password=settings.DB_PASS,
        database=settings.DB_NAME,
        host=settings.DB_HOST,
    )
    try:
        await conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
        logger.info("pgvector extension created or already exists.")
    except Exception as e:
        logger.error(f"Error creating pgvector extension: {e}")
    finally:
        await conn.close()


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

            cur.execute(f"CREATE DATABASE {database_name}")
            logger.info(f"Database '{database_name}' created.")
        else:
            logger.info(f"Database '{database_name}' already exists.")

        cur.close()
        conn.close()
    except Exception as e:
        logger.error(f"Error creating database: {e}")


from sqlalchemy import text


async def init_db() -> None:

    create_database(
        settings.DB_NAME,
        settings.DB_USER,
        settings.DB_PASS,
        settings.DB_HOST,
        settings.DB_PORT,
    )
    # After initializing the database, ensure the vector extension is created
    await create_extension()
    logger.info("Vector extension creation check attempted.")

    async_engine = create_async_engine(settings.ASYNC_DATABASE_URI, echo=True)

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logger.info("Database initialized and all tables created if they didn't exist.")
