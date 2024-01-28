from sqlalchemy import Column, Integer, String
from app.database.session import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    url = Column(String)
    description = Column(String)
    type = Column(String)
    sector = Column(String)
    headquarters = Column(String)
    founded = Column(String)
    notes = Column(String)
