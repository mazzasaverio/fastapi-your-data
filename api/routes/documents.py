from fastapi import APIRouter, Depends, HTTPException, status, Security
from sqlalchemy.orm import Session
from sqlalchemy import select
from api.models.documents import Documents, DocumentsResponse
from api.models.user import User
from api.database.connection import SessionLocal
from fastapi.security import APIKeyHeader
from typing import List
from api.config.logger_config import logger

docs_router = APIRouter(tags=["Docs"])
api_key_header = APIKeyHeader(name="Token", auto_error=False)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def get_current_user(
    token: str = Security(api_key_header), db: Session = Depends(get_db)
):
    logger.info(f"Received token: {token}")  # Debugging: Log the received token
    user = db.query(User).filter(User.token == token).first()
    if not user:
        logger.error(
            "Token validation failed"
        )  # Debugging: Log if token validation fails
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
    return user


@docs_router.get("/", response_model=List[DocumentsResponse])
async def retrieve_all_records(
    user: User = Depends(get_current_user), db: Session = Depends(get_db)
) -> List[DocumentsResponse]:
    records = db.query(Documents).all()
    return records
