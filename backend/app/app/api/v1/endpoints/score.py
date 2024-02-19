from fastapi import FastAPI
from app.api.v1.endpoints.pipeline.extract import (
    fetch_users_by_location,
    fetch_repo_readmes,
)
from app.api.v1.endpoints.pipeline.transform import (
    generate_embeddings,
    clean_readme_text,
)
from app.api.v1.endpoints.pipeline.load import load_to_database
from loguru import logger
from app.database.session import get_session
from app.core.config import settings

from fastapi import APIRouter

router = APIRouter()

session = get_session()


@router.get("/get_score")
async def get_score():
    return {"option1": "score1", "option2": "score2", "option3": "score3"}


@router.get("/start-etl-process")
async def start_etl_process():
    location = settings.LOCATION
    max_users = settings.MAX_USERS
    max_repos_per_user = settings.MAX_REPOS_PER_USER

    try:

        # Fetch users by location
        users = fetch_users_by_location(
            location, max_users, settings.GITHUB_ACCESS_TOKEN
        )
        logger.debug(f"Fetched {len(users)} users")

        # Fetch repository READMEs for the users
        readmes = fetch_repo_readmes(
            users, max_repos_per_user, settings.GITHUB_ACCESS_TOKEN
        )
        logger.debug(f"Fetched READMEs for {len(readmes)} repositories")

        # Process each README
        for readme in readmes:
            # Generate embeddings for the README
            embedding = generate_embeddings(readme["readme_text"])
            logger.debug(
                f"Generated embedding for {readme['username']}/{readme['repo_name']}"
            )

            # Clean the README text
            cleaned_readme = clean_readme_text(readme["readme_text"])
            logger.debug(
                f"Cleaned README for {readme['username']}/{readme['repo_name']}"
            )

            # Load the embeddings and READMEs into the database
            load_to_database(
                embedding,
                readme["readme_text"],
                cleaned_readme,
                session,
                readme["username"],
                readme["repo_name"],
                location,
            )
            logger.debug(
                f"Loaded data into database for {readme['username']}/{readme['repo_name']}"
            )

        logger.info("ETL process completed successfully")
    except Exception as e:
        logger.error(f"Error in ETL process: {e}")
    finally:
        session.close()
