from sqlmodel import create_engine, SQLModel, Session
from ..config.settings import settings
from api.models.docs_pdf import PdfDownload  # Import all models that need tables
from api.config.logger_config import logger

# Create the engine with the correct URL
engine = create_engine(settings.sqlalchemy_database_url, echo=True)


def conn():
    # Create tables for all imported models
    SQLModel.metadata.create_all(engine)
    logger.info("Database tables created")


def get_session():
    with Session(engine) as session:
        yield session


if __name__ == "__main__":
    conn()
