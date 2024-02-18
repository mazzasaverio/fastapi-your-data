from typing import Any, Generic, TypeVar, Union, Optional
from pydantic import BaseModel, ValidationError
import sqlalchemy.sql.selectable
from sqlalchemy import select, update, delete, func, and_, inspect, asc, desc, true
from sqlalchemy.exc import ArgumentError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from app.crud.utils import _extract_matching_columns_from_schema

ModelType = TypeVar("ModelType", bound=DeclarativeBase)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
DeleteSchemaType = TypeVar("DeleteSchemaType", bound=BaseModel)


class BaseCRUD(
    Generic[
        ModelType,
        CreateSchemaType,
        DeleteSchemaType,
    ]
):
    def __init__(self, model: type[ModelType]) -> None:
        self.model = model

    def _apply_sorting(
        self,
        stmt: sqlalchemy.sql.selectable.Select,
        sort_columns: Union[str, list[str]],
        sort_orders: Optional[Union[str, list[str]]] = None,
    ) -> sqlalchemy.sql.selectable.Select:
        """
        Apply sorting to a SQLAlchemy query based on specified column names and sort orders.

        Args:
            stmt: The SQLAlchemy Select statement to which sorting will be applied.
            sort_columns: A single column name or a list of column names on which to apply sorting.
            sort_orders: A single sort order ('asc' or 'desc') or a list of sort orders corresponding
                to the columns in sort_columns. If not provided, defaults to 'asc' for each column.

        Examples:
            Applying ascending sort on a single column:
            >>> stmt = _apply_sorting(stmt, 'name')

            Applying descending sort on a single column:
            >>> stmt = _apply_sorting(stmt, 'age', 'desc')

            Applying mixed sort orders on multiple columns:
            >>> stmt = _apply_sorting(stmt, ['name', 'age'], ['asc', 'desc'])
        """
        if sort_orders and not sort_columns:
            raise ValueError("Sort orders provided without corresponding sort columns.")

        if sort_columns:
            if not isinstance(sort_columns, list):
                sort_columns = [sort_columns]

            if sort_orders:
                if not isinstance(sort_orders, list):
                    sort_orders = [sort_orders] * len(sort_columns)
                if len(sort_columns) != len(sort_orders):
                    raise ValueError(
                        "The length of sort_columns and sort_orders must match."
                    )

                for idx, order in enumerate(sort_orders):
                    if order not in ["asc", "desc"]:
                        raise ValueError(
                            f"Invalid sort order: {order}. Only 'asc' or 'desc' are allowed."
                        )

            validated_sort_orders = (
                ["asc"] * len(sort_columns) if not sort_orders else sort_orders
            )

            for idx, column_name in enumerate(sort_columns):
                column = getattr(self.model, column_name, None)
                if not column:
                    raise ArgumentError(f"Invalid column name: {column_name}")

                order = validated_sort_orders[idx]
                stmt = stmt.order_by(asc(column) if order == "asc" else desc(column))

        return stmt

    async def create_record(
        self, db: AsyncSession, object: CreateSchemaType
    ) -> ModelType:
        """
        Create a new record.
        """
        object_dict = object.model_dump()
        db_object: ModelType = self.model(**object_dict)
        db.add(db_object)
        await db.commit()
        return db_object

    async def delete_record(self, db: AsyncSession, **kwargs: Any) -> None:
        """
        Delete a record.
        """
        stmt = delete(self.model).filter_by(**kwargs)
        await db.execute(stmt)
        await db.commit()

    async def get(self, db: AsyncSession, id: int) -> Optional[ModelType]:
        """
        Fetch a single record by id.
        """
        result = await db.execute(select(self.model).filter(self.model.id == id))
        return result.scalars().first()

    async def get_multi(
        self,
        db: AsyncSession,
        offset: int = 0,
        limit: int = 100,
        schema_to_select: Optional[type[BaseModel]] = None,
        sort_columns: Optional[Union[str, list[str]]] = None,
        sort_orders: Optional[Union[str, list[str]]] = None,
        return_as_model: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Fetch multiple records based on filters, with optional sorting, pagination, and model conversion.

        Args:
            db: The SQLAlchemy async session.
            offset: Number of rows to skip before fetching. Must be non-negative.
            limit: Maximum number of rows to fetch. Must be non-negative.
            schema_to_select: Pydantic schema for selecting specific columns.
            sort_columns: Single column name or a list of column names for sorting.
            sort_orders: Single sort direction ('asc' or 'desc') or a list of directions corresponding to the columns in sort_columns. Defaults to 'asc'.
            return_as_model: If True, returns the data as instances of the Pydantic model.
            **kwargs: Filters to apply to the query.

        Examples:
            Fetch the first 10 users:
            ```python
            users = await crud.get_multi(db, 0, 10)
            ```

            Fetch next 10 users with sorting:
            ```python
            users = await crud.get_multi(db, 10, 10, sort_columns='username', sort_orders='desc')
            ```

            Fetch users with filtering and multiple column sorting:
            ```python
            users = await crud.get_multi(db, 0, 10, is_active=True, sort_columns=['username', 'email'], sort_orders=['asc', 'desc'])
            ```
        """
        if limit < 0 or offset < 0:
            raise ValueError("Limit and offset must be non-negative.")

        to_select = _extract_matching_columns_from_schema(self.model, schema_to_select)
        stmt = select(*to_select).filter_by(**kwargs)

        if sort_columns:
            stmt = self._apply_sorting(stmt, sort_columns, sort_orders)

        stmt = stmt.offset(offset).limit(limit)
        result = await db.execute(stmt)
        data = [dict(row) for row in result.mappings()]

        if return_as_model:
            if not schema_to_select:
                raise ValueError(
                    "schema_to_select must be provided when return_as_model is True."
                )
            try:
                data = [schema_to_select.model_construct(**row) for row in data]
            except ValidationError as e:
                raise ValueError(
                    f"Data validation error for schema {schema_to_select.__name__}: {e}"
                )

        return {"data": data}
