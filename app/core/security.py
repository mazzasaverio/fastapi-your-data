from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from config import settings
import httpx

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def decode_keycloak_token(token: str):
    try:
        payload = jwt.decode(
            token, settings.KEYCLOAK_SECRET, algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_keycloak_token(token)
    username: str = payload.get("preferred_username")
    if username is None:
        raise HTTPException(status_code=400, detail="Invalid JWT token")
    user_roles: list = payload.get("roles", [])
    # Additional logic to handle user roles can be implemented here
    return {"username": username, "roles": user_roles}


def is_user_authorized(roles: list, required_roles: set):
    return set(roles).intersection(required_roles)
