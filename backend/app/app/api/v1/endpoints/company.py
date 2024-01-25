# backend/app/app/api/v1/endpoints/company.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import AsyncSessionFactory
from app.crud.company_crud import CompanyCRUD
from app.schemas.company_schema import CompanyResponse
from app.core.security import get_api_key

company_router = APIRouter()


def sess_db():
    db = AsyncSessionFactory()
    try:
        yield db
    finally:
        db.close()


@company_router.post("/", response_model=CompanyResponse)
async def add_company(
    company_create: CompanyResponse, sess: Session = Depends(sess_db)
):
    company_crud = CompanyCRUD(sess)
    return company_crud.create_company(company_create)


@company_router.delete("/{company_id}")
async def remove_company(company_id: int, sess: Session = Depends(sess_db)):
    company_crud = CompanyCRUD(sess)
    if not company_crud.delete_company(company_id):
        raise HTTPException(status_code=404, detail="Company not found")
    return {"message": "Company deleted successfully"}
