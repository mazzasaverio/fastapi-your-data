from sqlalchemy.ext.declarative import declarative_base
from app.core.config import Settings
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

settings = Settings()
# Define the base class for your models
Base = declarative_base()

# Reusing the AsyncEngine instance
engine = create_async_engine(settings.ASYNC_DATABASE_URI, future=True, echo=True)

# Creating an async session factory
AsyncSessionFactory = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from app.core.config import settings

# # Define the base class for your models
# Base = declarative_base()

# # Create a synchronous engine instance
# engine = create_engine(settings.DATABASE_URI, future=True, echo=True)

# # Creating a synchronous session factory
# LocalSession = sessionmaker(bind=engine)


# def get_session():
#     """Get a new session"""
#     return LocalSession()
