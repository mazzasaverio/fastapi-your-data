from fastapi import APIRouter
from .endpoints import data_ingestion, similarity_score

api_router = APIRouter()

# Including router for data ingestion
api_router.include_router(
    data_ingestion.router, prefix="/data_ingestion", tags=["Data Ingestion"]
)

# Including router for similarity score calculations
api_router.include_router(
    similarity_score.router, prefix="/similarity_score", tags=["Similarity Score"]
)
