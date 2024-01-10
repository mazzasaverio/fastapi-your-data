from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database.sqlalchemy_connection import SessionFactory
from app.repository.users import UsersRepository
from app.schemas.user import UserCreate, UserResponse
from loguru import logger


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


user_router = APIRouter(tags=["User"])


@user_router.post("/signup", response_model=UserResponse)
async def sign_up_user(user_data: UserCreate, sess: Session = Depends(sess_db)):
    users_repo = UsersRepository(sess)
    logger.info("Creating new user")
    try:
        # Check if user already exists
        if users_repo.get_user_by_email(user_data.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with supplied email already exists",
            )
        # Create new user
        new_user = users_repo.add_user(user_data)
        return UserResponse(email=new_user.email, token=new_user.token)
    except Exception as e:
        logger.error(f"Failed to sign up user: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")


@user_router.post("/signin", response_model=UserResponse)
async def sign_in_user(email: str, password: str, sess: Session = Depends(sess_db)):
    users_repo = UsersRepository(sess)
    # Verify email
    user = users_repo.get_user_by_email(email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    # Verify password
    if not users_repo.hash_password.verify_hash(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password"
        )
    return UserResponse(email=user.email, token=user.token)
