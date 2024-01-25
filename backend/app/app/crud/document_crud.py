from sqlalchemy.orm import Session
from app.models.document_model import Documents
from loguru import logger


class DocumentsRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_documents(self):
        try:
            documents = self.db.query(Documents).limit(5).all()
            return documents
        except Exception as e:
            logger.error(f"Error fetching documents: {e}")
            raise
