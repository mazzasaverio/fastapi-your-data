from sqlalchemy.orm import Session
from sqlalchemy import select
from etl.github_data.database.models import Repository, User
from loguru import logger
from datetime import datetime


def load_to_database(
    embedding,
    raw_readme,
    cleaned_readme,
    db_session: Session,
    username,
    repo_name,
    location,
):
    """
    Load the embedding and readme data into the database synchronously.

    :param embedding: The embedding to load.
    :param raw_readme: The raw README text.
    :param cleaned_readme: The cleaned README text.
    :param db_session: The database session (Session).
    :param username: The username of the GitHub user.
    :param repo_name: The name of the GitHub repository.
    """
    logger.debug(f"Attempting to load embedding for {username}/{repo_name}")

    # Check if user exists in the database, otherwise create a new user
    user_stmt = select(User).where(User.username == username)
    result = db_session.execute(user_stmt)
    user = result.scalars().first()

    if not user:
        logger.debug(f"User {username} not found, creating a new user.")

        user = User(username=username, location=location)
        db_session.add(user)
        db_session.commit()
        # Re-fetch the user after commit to ensure it has an ID
        result = db_session.execute(user_stmt)
        user = result.scalars().first()

    # Create a new repository record every time
    logger.debug(f"Creating a new repository record for {username}/{repo_name}.")
    repository = Repository(
        name=repo_name,
        user_id=user.user_id,
        username=username,
        readme_raw=raw_readme,
        readme_cleaned=cleaned_readme,
        readme_embedding=embedding,
        updated_at=datetime.utcnow(),
    )
    db_session.add(repository)
    db_session.commit()
    logger.info(
        f"Successfully loaded embedding and README data into database for {username}/{repo_name}"
    )
