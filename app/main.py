from fastapi import FastAPI
from .api.v1 import dataset_routes

app = FastAPI()

app.include_router(dataset_routes.router, prefix="/v1")
