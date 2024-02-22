from sqlalchemy import Column, Integer, String, Date, Text
from pgvector.sqlalchemy import Vector
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserModel(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    survey_id = Column(Integer, index=True)
    survey_date = Column(Date)
    survey_text = Column(Text)
    survey_embedding = Column(Vector)
