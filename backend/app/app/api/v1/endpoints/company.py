from fastapi import APIRouter, HTTPException, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.base_crud import BaseCRUD
from app.models.company_model import Company
from app.schemas.company_schema import CompanyCreate, CompanyResponse
from app.database.session import AsyncSessionFactory
from loguru import logger

router = APIRouter()


# Dependency for database session
async def get_db_session():
    async with AsyncSessionFactory() as session:
        yield session


@router.post("/", response_model=CompanyResponse)
async def create_company(
    company: CompanyCreate, db: AsyncSession = Depends(get_db_session)
):
    crud = BaseCRUD(Company)
    new_company = await crud.create_record(db, company)
    return new_company


@router.delete("/{company_id}")
async def delete_company(company_id: int, db: AsyncSession = Depends(get_db_session)):
    crud = BaseCRUD(Company)
    await crud.delete_record(db, id=company_id)
    return {"status": "success", "message": "Company deleted"}


@router.get("/", response_model=list[CompanyResponse])
async def get_companies(db: AsyncSession = Depends(get_db_session)):
    crud = BaseCRUD(Company)
    companies = await crud.get_multi(db)
    return companies["data"]
