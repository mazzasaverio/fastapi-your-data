from pydantic import BaseModel


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
