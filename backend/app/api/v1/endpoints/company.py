from fastapi import APIRouter, HTTPException, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.crud.base_crud import BaseCRUD
from backend.app.models.company_model import Company
from backend.app.schemas.company_schema import (
    CompanyCreate,
    CompanyResponse,
    CompanyUpdate,
)
from backend.app.database.session import AsyncSessionFactory
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


@router.put("/{company_id}", response_model=CompanyResponse)
async def update_company(
    company_id: int,
    company_update: CompanyUpdate,
    db: AsyncSession = Depends(get_db_session),
):
    crud = BaseCRUD(Company)
    try:
        existing_company = await crud.get(db, id=company_id)

        if not existing_company:
            raise HTTPException(status_code=404, detail="Company not found")

        for var, value in vars(company_update).items():
            setattr(existing_company, var, value) if value else None

        db.add(existing_company)
        await db.commit()
        await db.refresh(existing_company)

        return existing_company
    except Exception as e:
        logger.error(f"Error updating company: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
