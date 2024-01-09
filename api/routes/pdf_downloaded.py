from fastapi import APIRouter, Depends, HTTPException, Request, status
from api.models.docs_pdf import PdfDownload
from api.database.connection import get_session
from typing import List
from sqlmodel import select
from api.config.logger_config import logger

docs_router = APIRouter(tags=["Docs"])


@docs_router.get("/", response_model=List[PdfDownload])
async def retrieve_all_events(session=Depends(get_session)) -> List[PdfDownload]:
    statement = select(PdfDownload)
    events = session.exec(statement).all()
    logger.info(f"###### Retrieved {len(events)} events")
    return events
