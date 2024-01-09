# app/services/basic_crud_operations.py
from typing import Type, TypeVar, Generic, List
from sqlalchemy.orm import Session
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)  # T is a TypeVar bound to BaseModel (from Pydantic)


class CRUDOperations(Generic[T]):
    def __init__(self, model: Type[T]):
        """
        CRUD object with generic methods to Create, Read, Update, Delete (CRUD).

        :param model: A SQLAlchemy model class
        """
        self.model = model

    def create(self, db: Session, *, obj_in: T) -> T:
        """
        Create a new database record.

        :param db: SQLAlchemy database session.
        :param obj_in: Pydantic model of the object to be created.
        :return: The created database record.
        """
        db_obj = self.model(**obj_in.dict())  # Create a new SQLAlchemy model instance
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def read(self, db: Session, id: int) -> T:
        """
        Get a single record by ID.

        :param db: SQLAlchemy database session.
        :param id: ID of the record to retrieve.
        :return: The database record object.
        """
        return db.query(self.model).filter(self.model.id == id).first()

    def update(self, db: Session, *, db_obj: T, obj_in: T) -> T:
        """
        Update a database record.

        :param db: SQLAlchemy database session.
        :param db_obj: SQLAlchemy model instance to update.
        :param obj_in: Pydantic model of the object with updated fields.
        :return: The updated database record.
        """
        obj_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            setattr(db_obj, field, obj_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, id: int) -> T:
        """
        Delete a record by ID.

        :param db: SQLAlchemy database session.
        :param id: ID of the record to delete.
        :return: The deleted object.
        """
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def read_all(self, db: Session) -> List[T]:
        """
        Get all records of the model.

        :param db: SQLAlchemy database session.
        :return: List of database record objects.
        """
        return db.query(self.model).all()
