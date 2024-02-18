from app.api.v1.api import api_router as api_router_v1
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database.init_db import init_db


# @asynccontextmanager
# async def app_lifespan(app: FastAPI):
#     # Database initialization
#     await init_db()

#     yield


# app = FastAPI(lifespan=app_lifespan)

app = FastAPI()

app.include_router(api_router_v1)


@app.get("/metrics")
def metrics():
    return {"message": "Metrics endpoint"}


@app.get("/")
async def home():
    return "Welcome!"
