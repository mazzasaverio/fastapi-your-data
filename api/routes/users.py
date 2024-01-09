from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from api.models.user import User, UserCreate, UserResponse
from api.database.connection import SessionLocal
import uuid

user_router = APIRouter(tags=["User"])


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@user_router.post("/signup", response_model=UserResponse)
async def sign_new_user(user_data: UserCreate, db: Session = Depends(get_db)):
    with db as session:
        existing_user = session.execute(
            select(User).where(User.email == user_data.email)
        ).scalar()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with supplied email already exists",
            )

        new_user = User(
            email=user_data.email, password=user_data.password, token=str(uuid.uuid4())
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)

    return UserResponse(email=new_user.email, token=new_user.token)


@user_router.post("/signin", response_model=UserResponse)
async def sign_user_in(
    email: str, password: str, db: Session = Depends(get_db)
) -> UserResponse:
    user = db.execute(select(User).where(User.email == email)).scalar()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    if user.password != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password"
        )
    return UserResponse(email=user.email, token=user.token)
