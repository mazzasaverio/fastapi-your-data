from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from loguru import logger
import uvicorn
from starlette.middleware.base import BaseHTTPMiddleware
from app.api.v1.endpoints.company import router as company_router
from fastapi.middleware.cors import CORSMiddleware
from uuid import uuid4
import sys

app = FastAPI()


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid4())
        logger.info(f"Request [{request_id}] start: {request.method} {request.url}")
        try:
            response = await call_next(request)
            logger.info(
                f"Request [{request_id}] completed: Status code {response.status_code}"
            )
            return response
        except Exception as e:
            logger.error(f"Request [{request_id}] failed: {e}")
            raise e


app.add_middleware(LoggingMiddleware)

# Include routers
app.include_router(company_router, prefix="/companies")

# CORS middleware configuration
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


# # Logger configuration
# logger.remove()
# logger.add(sys.stdout, level="INFO", format="{time} | {level} | {message}")
# logger.add("logs/app_{time}.log", rotation="1 day", retention="10 days", level="INFO")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)
