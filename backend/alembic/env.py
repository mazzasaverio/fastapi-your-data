from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine
from backend.app.core.config import Settings
from backend.app.database.session import Base

# Models
from backend.app.models import company_model, document_model

# Logging
from logging.config import fileConfig

# Configuration
config = context.config
if config.config_file_name:
    fileConfig(config.config_file_name, disable_existing_loggers=False)

# Metadata and database settings
target_metadata = Base.metadata
settings = Settings()
db_url = str(settings.ASYNC_DATABASE_URI)


# Migration functions
def run_migrations_offline():
    """Run migrations in offline mode."""
    context.configure(
        url=db_url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in online mode."""
    engine = create_async_engine(db_url, echo=True, future=True)
    async with engine.connect() as connection:
        await connection.run_sync(do_run_migrations)


# Main execution
if context.is_offline_mode():
    run_migrations_offline()
else:
    import asyncio

    asyncio.run(run_migrations_online())
