# init_db.py
from backend.app.app.database.session import engine, Base
from backend.app.app.models.documents import Documents
from loguru import logger


def init_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)
    logger.info("All tables created")


if __name__ == "__main__":
    init_db()
