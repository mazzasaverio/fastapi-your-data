# init_db.py
from app.database.sqlalchemy_connection import engine, Base
from app.database.models.user import User
from app.database.models.documents import Documents
from loguru import logger


def init_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)
    logger.info("All tables created")


if __name__ == "__main__":
    init_db()
