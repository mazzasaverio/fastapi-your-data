from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from config.settings import settings

# Define the base class for your models
Base = declarative_base()

# Create the SQLAlchemy engine
engine = create_engine(settings.sqlalchemy_database_url, echo=False)

# Create a configured "SessionFactory" class
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
