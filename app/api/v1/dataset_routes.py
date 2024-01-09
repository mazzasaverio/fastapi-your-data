# app/api/v1/dataset_routes.py
from fastapi import APIRouter, Depends
from app.services.basic_crud_operations import CRUDOperations
from app.models.sql_models.docs_categ_metadata import (
    PdfDownload,
)  # Import the necessary model
from app.core.database.orm_connection import session_scope

router = APIRouter()


# Example route
@router.get("/datasets")
async def get_datasets():
    with session_scope() as session:
        crud_service = CRUDOperations(PdfDownload)
        return crud_service.read_all(session)
