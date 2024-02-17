from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from etl.github_data.config.settings import Config

# Define the base class for your models
Base = declarative_base()

# Create a synchronous engine instance
engine = create_engine(Config.DATABASE_URI, future=True, echo=True)

# Creating a synchronous session factory
LocalSession = sessionmaker(bind=engine)


def get_session():
    """Get a new session"""
    return LocalSession()
