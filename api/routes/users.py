from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import Session, select
from api.models.user import User
from api.database.connection import get_session

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

    # Add new user to the database
    session.add(data)
    session.commit()
    session.refresh(data)
    return {"message": "User successfully registered!"}


@user_router.post("/signin")
async def sign_user_in(user: User) -> dict:
    if users[user.email] not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with supplied username does not exist",
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )
