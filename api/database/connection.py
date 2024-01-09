from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from api.config.settings import settings

# Define the base class for your models
Base = declarative_base()

# Create the SQLAlchemy engine
engine = create_engine(settings.sqlalchemy_database_url, echo=False)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Function to create all tables
def init_db():
    import api.models  # Import all the modules that define your SQLAlchemy models

    Base.metadata.create_all(bind=engine)


# Dependency to get a database session
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
