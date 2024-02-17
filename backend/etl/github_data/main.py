from etl.github_data.pipeline.extract import fetch_users_by_location, fetch_repo_readmes
from etl.github_data.pipeline.transform import generate_embeddings, clean_readme_text
from etl.github_data.pipeline.load import load_to_database
from etl.github_data.database.session import get_session
from etl.github_data.config.settings import Config
from loguru import logger
from etl.github_data.config.settings import LogConfig  # Ensure the logger is configured

import os
from dotenv import load_dotenv

load_dotenv()

session = get_session()


def main():
    location = Config.LOCATION
    max_users = Config.MAX_USERS
    max_repos_per_user = Config.MAX_REPOS_PER_USER

    try:

        # Fetch users by location
        users = fetch_users_by_location(location, max_users, Config.GITHUB_ACCESS_TOKEN)
        logger.debug(f"Fetched {len(users)} users")

        # Fetch repository READMEs for the users
        readmes = fetch_repo_readmes(
            users, max_repos_per_user, Config.GITHUB_ACCESS_TOKEN
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


if __name__ == "__main__":
    main()
