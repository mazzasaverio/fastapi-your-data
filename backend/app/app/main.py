from app.api.v1.api import api_router as api_router_v1
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database.init_db import init_db
from fastapi.responses import RedirectResponse

# from fastapi_pagination import add_pagination
import os
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    await init_db()

    yield


app = FastAPI(lifespan=app_lifespan)


app.include_router(api_router_v1)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/metrics")
def metrics():
    return {"message": "Metrics endpoint"}


@app.get("/")
async def home():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)
