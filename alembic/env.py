from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys

# Important: Add the app directory to the sys.path
sys.path.append(os.getcwd())

from api.core.database.connection import Base  # Import the Base from your models
from api.config.settings import settings  # Import your settings

# Alembic Config object
config = context.config

# Overwrite the sqlalchemy.url from alembic.ini with the one from settings
config.set_main_option("sqlalchemy.url", settings.sqlalchemy_database_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# Set the target metadata for autogenerate
target_metadata = Base.metadata


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
