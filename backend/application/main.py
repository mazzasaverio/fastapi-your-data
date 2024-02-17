from application.sub_app_1 import main as sub_app_1_main
from application.gateway.api_router import call_api_gateway
from application.controller import platform
from fastapi import FastAPI, Depends


app = FastAPI()
app.include_router(platform.router, dependencies=[Depends(call_api_gateway)])

app.mount("/sub_app_1", sub_app_1_main.app)
