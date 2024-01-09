from sqlmodel import create_engine, SQLModel, Session
from ..config.settings import settings
from api.models.docs_pdf import PdfDownload
from api.models.user import User
from api.config.logger_config import logger

engine = create_engine(settings.sqlalchemy_database_url, echo=False)


def conn():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


if __name__ == "__main__":
    conn()
