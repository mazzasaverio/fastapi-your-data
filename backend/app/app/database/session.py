from sqlalchemy.ext.declarative import declarative_base
from backend.app.app.core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

# Define the base class for your models
Base = declarative_base()

# Reusing the AsyncEngine instance
engine = create_async_engine(settings.sqlalchemy_database_url, future=True, echo=True)

# Creating an async session factory
AsyncSessionFactory = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
