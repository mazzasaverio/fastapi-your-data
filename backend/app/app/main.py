from fastapi import FastAPI, Request, Depends
from fastapi.responses import RedirectResponse, JSONResponse
from loguru import logger
import sys
from uuid import uuid4
import uvicorn
from backend.app.app.api.v1.endpoints.documents import docs_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Include routers
app.include_router(docs_router, prefix="/documents")

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


# Simple hello endpoint
@app.get("/hello")
async def hello():
    return {"message": "Ciao"}


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


# Request logging middleware
@app.middleware("http")
async def log_middleware(request: Request, call_next):
    log_id = str(uuid4())
    with logger.contextualize(log_id=log_id):
        logger.info("Request to access " + request.url.path)
        try:
            response = await call_next(request)
        except Exception as ex:
            logger.error(f"Request to " + request.url.path + " failed: {ex}")
            response = JSONResponse(content={"success": False}, status_code=500)
        finally:
            logger.info("Successfully accessed " + request.url.path)
            return response


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)
