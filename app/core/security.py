# app/core/security.py
from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
from app.config.settings import settings

api_key_header = APIKeyHeader(name="X-API-Key")


async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header != settings.api_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key_header
