from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from loguru import logger

from app.api.routes.documents import docs_router
from app.api.routes.users import user_router

from fastapi import FastAPI, Request
from loguru import logger
from uuid import uuid4
import sys
from fastapi.responses import JSONResponse
import uvicorn


app = FastAPI()

app.include_router(docs_router, prefix="/documents")
app.include_router(user_router, prefix="/user")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specify domains if you want to restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/metrics")
def metrics():
    return {"message": "This is a dummy metrics endpoint."}


@app.get("/")
async def home():
    return RedirectResponse(url="/docs")


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
    uvicorn.run("app_main:app", host="0.0.0.0", port=8080, reload=True)
