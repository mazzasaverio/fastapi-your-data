from pydantic import BaseModel


# Model for creating a new company
class CompanyCreate(BaseModel):
    name: str
    url: str
    description: str
    type: str
    sector: str
    headquarters: str
    founded: str
    notes: str


# Model for updating an existing company
class CompanyUpdate(BaseModel):
    name: str
    url: str
    description: str
    type: str
    sector: str
    headquarters: str
    founded: str
    notes: str


# Model for company responses
class CompanyResponse(BaseModel):
    id: int
    name: str
    url: str
    description: str
    type: str
    sector: str
    headquarters: str
    founded: str
    notes: str
