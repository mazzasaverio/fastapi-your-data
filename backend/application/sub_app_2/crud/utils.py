from typing import Any, Union, Optional
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel


def _extract_matching_columns_from_schema(
    model: type[DeclarativeBase], schema: Optional[Union[type[BaseModel], list]]
) -> list[Any]:
    """
    Retrieves a list of ORM column objects from a SQLAlchemy model that match the field names in a given Pydantic schema.

    Args:
        model: The SQLAlchemy ORM model containing columns to be matched with the schema fields.
        schema: The Pydantic schema containing field names to be matched with the model's columns.

    Returns:
        A list of ORM column objects from the model that correspond to the field names defined in the schema.
    """
    column_list = list(model.__table__.columns)
    if schema is not None:
        if isinstance(schema, list):
            schema_fields = schema
        else:
            schema_fields = schema.model_fields.keys()

        column_list = []
        for column_name in schema_fields:
            if hasattr(model, column_name):
                column_list.append(getattr(model, column_name))

    return column_list
