# orm_connection.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager
from .api.config import Config

# Generic SQL database URL from Config
DATABASE_URL = Config.SQLALCHEMY_DATABASE_URL

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# SessionLocal class - each instance of this class will be a database session
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models to inherit
Base = declarative_base()

# Create tables
Base.metadata.create_all(engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
