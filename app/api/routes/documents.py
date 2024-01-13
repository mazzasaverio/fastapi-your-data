from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database.sqlalchemy_connection import SessionFactory
from app.repository.documents import DocumentsRepository
from app.schemas.documents import DocumentsResponse
from app.core.security import get_api_key
from loguru import logger

docs_router = APIRouter()


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@docs_router.get("/", response_model=List[DocumentsResponse])
async def retrieve_all_documents(
    api_key: str = Depends(get_api_key),
    sess: Session = Depends(sess_db),
):
    documents_repo = DocumentsRepository(sess)
    documents = documents_repo.get_all_documents()
    logger.info(f"Retrieved all documents {len(documents)}")
    logger.info(f"Retrieved all documents {documents}")
    return documents
