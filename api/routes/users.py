from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import Session, select
from api.models.user import User
from api.database.connection import get_session
import uuid

user_router = APIRouter(tags=["User"])
users = {}


@user_router.post("/signup")
async def sign_new_user(data: User, session: Session = Depends(get_session)) -> dict:
    # Check if the user already exists in the database
    existing_user = session.exec(select(User).where(User.email == data.email)).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied email already exists",
        )

    # Generate a unique token for the new user
    data.token = str(uuid.uuid4())

    # Add new user to the database
    session.add(data)
    session.commit()
    session.refresh(data)
    return {"message": "User successfully registered!"}


@user_router.post("/signin")
async def sign_user_in(
    email: str, password: str, session: Session = Depends(get_session)
) -> dict:
    user = session.exec(select(User).where(User.email == email)).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    if user.password != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )
    return {"message": "User successfully signed in!", "token": user.token}
