from fastapi import APIRouter, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordRequestForm
import httpx
from app.core.security import get_current_user
from config import settings
from app.schemas.user import UserResponse

auth_router = APIRouter()


def get_keycloak_token(username: str, password: str):
    data = {
        "client_id": settings.KEYCLOAK_CLIENT_ID,
        "client_secret": settings.KEYCLOAK_CLIENT_SECRET,
        "grant_type": "password",
        "username": username,
        "password": password,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    token_endpoint = f"{settings.KEYCLOAK_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/token"
    response = httpx.post(token_endpoint, data=data, headers=headers)
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail="Keycloak authentication failed"
        )
    return response.json()


@auth_router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    keycloak_response = get_keycloak_token(form_data.username, form_data.password)
    return {
        "access_token": keycloak_response["access_token"],
        "refresh_token": keycloak_response.get("refresh_token"),
        "token_type": "bearer",
    }


@auth_router.get("/users/me", response_model=UserResponse)
async def read_users_me(current_user: UserResponse = Depends(get_current_user)):
    return current_user
