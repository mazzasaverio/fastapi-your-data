# backend/app/app/crud/company_crud.py
from sqlalchemy.orm import Session
from app.models.company_model import Company
from loguru import logger


class CompanyCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create_company(self, company_create):
        new_company = Company(**company_create.dict())
        self.db.add(new_company)
        self.db.commit()
        self.db.refresh(new_company)
        return new_company

    def delete_company(self, company_id: int):
        company = self.db.query(Company).filter(Company.id == company_id).first()
        if company:
            self.db.delete(company)
            self.db.commit()
            return True
        return False
