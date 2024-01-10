from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.database.models.user import User
from app.utils.hash_password import HashPassword
from loguru import logger
from uuid import uuid4
from sqlalchemy import select


class UsersRepository:
    def __init__(self, sess: Session):
        self.sess: Session = sess
        self.hash_password = HashPassword()

    def generate_token(self):
        # Generate a unique token for the user, you might want to use JWT or other methods
        return str(uuid4())

    def add_user(self, user_data):
        hashed_password = self.hash_password.create_hash(user_data.password)
        token = self.generate_token()
        new_user = User(email=user_data.email, password=hashed_password, token=token)

        try:
            self.sess.add(new_user)
            self.sess.commit()
            self.sess.refresh(new_user)
            return new_user
        except Exception as e:
            logger.error(f"Error adding new user: {e}")
            self.sess.rollback()
            raise

    def get_user_by_email(self, email):
        try:
            existing_user = self.sess.execute(
                select(User).where(User.email == email)
            ).scalar()

            return existing_user
        except Exception as e:
            logger.error(f"Error fetching user by email: {e}")
            raise
