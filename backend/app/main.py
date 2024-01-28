from fastapi import FastAPI, Request, Depends
from fastapi.responses import RedirectResponse, JSONResponse
from loguru import logger
import sys
from uuid import uuid4
import uvicorn

# from backend.app.api.v1.endpoints.document import docs_router
from app.api.v1.endpoints.company import router as company_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Include routers
app.include_router(company_router, prefix="/companies")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specify domains if you want to restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Metrics endpoint
@app.get("/metrics")
def metrics():
    return {"message": "This is a dummy metrics endpoint."}


# Root endpoint
@app.get("/")
async def home():
    return RedirectResponse(url="/docs")


# Logger configuration
logger.remove()
logger.add(
    sys.stdout,
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
)
logger.add(
    "logs/esg_spider_{time}.log",
    rotation="1 day",
    retention="7 days",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)
