from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from api.database.connection import conn
from api.routes.docs import docs_router
from contextlib import asynccontextmanager
from api.config.logger_config import logger
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    conn()
    yield


app = FastAPI(lifespan=lifespan)

# Register routes
app.include_router(docs_router, prefix="/docs")


@app.get("/")
async def home():
    return RedirectResponse(url="/docs/")


if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=8080, reload=True)
