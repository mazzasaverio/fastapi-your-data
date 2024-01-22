from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.app.app.database.session import AsyncSessionFactory
from backend.app.app.repository.documents import DocumentsRepository
from backend.app.app.schemas.documents import DocumentsResponse
from backend.app.app.core.security import get_api_key
from loguru import logger

docs_router = APIRouter()


def sess_db():
    db = AsyncSessionFactory()
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
