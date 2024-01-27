from pydantic import BaseModel, Field
from typing import Optional


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


class CompanyUpdate(BaseModel):
    name: Optional[str] = Field(None, description="The name of the company")
    url: Optional[str] = Field(None, description="The URL of the company")
    description: Optional[str] = Field(
        None, description="The description of the company"
    )
    type: Optional[str] = Field(None, description="The type of the company")
    sector: Optional[str] = Field(None, description="The sector of the company")
    headquarters: Optional[str] = Field(
        None, description="The headquarters of the company"
    )
    founded: Optional[str] = Field(None, description="The founding date of the company")
    notes: Optional[str] = Field(None, description="Additional notes about the company")


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
