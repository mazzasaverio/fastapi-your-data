from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.sqlalchemy_connection import SessionFactory
from app.repository.documents import DocumentsRepository
from app.schemas.documents import DocumentsResponse
from typing import List
from loguru import logger


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


docs_router = APIRouter()


@docs_router.get("/", response_model=List[DocumentsResponse])
async def retrieve_all_documents(sess: Session = Depends(sess_db)):
    documents_repo = DocumentsRepository(sess)
    documents = documents_repo.get_all_documents()
    logger.info(f"Retrieved {len(documents)} documents")
    return documents
