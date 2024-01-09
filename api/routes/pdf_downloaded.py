from fastapi import APIRouter, Depends, HTTPException, status, Security
from fastapi.security import APIKeyHeader
from sqlmodel import Session, select
from typing import List
from api.models.docs_pdf import PdfDownload
from api.models.user import User
from api.database.connection import get_session
from api.config.logger_config import logger

# Router setup for documents
docs_router = APIRouter(tags=["Docs"])

# Header for token authentication
api_key_header = APIKeyHeader(name="Token", auto_error=False)


# Dependency to get the current user based on the token
async def get_current_user(
    token: str = Security(api_key_header), session: Session = Depends(get_session)
):
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="No token provided"
        )

    user = session.exec(select(User).where(User.token == token)).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )

    return user


# Endpoint to retrieve all documents, accessible only with valid token
@docs_router.get("/", response_model=List[PdfDownload])
async def retrieve_all_records(
    user: User = Depends(get_current_user), session: Session = Depends(get_session)
) -> List[PdfDownload]:
    statement = select(PdfDownload)
    events = session.exec(statement).all()
    logger.info(f"Retrieved {len(events)} records from the database")
    return events
