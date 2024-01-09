from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from api.database.connection import init_db
from api.routes.documents import docs_router
from api.routes.users import user_router
from contextlib import asynccontextmanager
from api.config.logger_config import logger
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)

# Register routes
app.include_router(docs_router, prefix="/documents")
app.include_router(user_router, prefix="/user")


@app.get("/metrics")
def metrics():
    return {"message": "This is a dummy metrics endpoint."}


@app.get("/")
async def home():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=8080, reload=True)
