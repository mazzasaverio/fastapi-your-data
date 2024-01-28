# init_db.py
from app.database.session import engine, Base
from app.models.document_model import Documents
from loguru import logger


def init_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)
    logger.info("All tables created")


if __name__ == "__main__":
    init_db()
