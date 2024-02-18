from app.sub_app_1.api.v1.api import api_router as api_router_v1
from fastapi.responses import RedirectResponse
from fastapi import FastAPI

app = FastAPI()

# Add Routers
app.include_router(api_router_v1)


@app.get("/metrics")
def metrics():
    return {"message": "Metrics endpoint"}


@app.get("/")
async def home():
    return "Welcome to Sub App 1"
