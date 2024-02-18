from fastapi import APIRouter
from .endpoints import score

api_router = APIRouter()
api_router.include_router(score.router, tags=["score"])
