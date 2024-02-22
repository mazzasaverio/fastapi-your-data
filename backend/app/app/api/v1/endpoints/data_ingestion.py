from sqlalchemy import select
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Query
from typing import List
from app.api.dependencies import (
    get_db,
    get_embedding_service,
    get_text_process_service,
    get_extraction_service,
)
from app.models.github_model import GitRepository
from app.crud.github_crud import GitHubCRUD
from app.services.text_process_service import TextProcessService
from app.services.embedding_service import EmbeddingService
from app.services.extraction_service import ExtractionService
import asyncio
from loguru import logger

router = APIRouter()


@router.post("/data_ingestion")
async def data_ingestion(
    location: str = Query(
        "Milan", description="The location to filter GitHub users by."
    ),
    max_users: int = Query(2, description="The maximum number of users to fetch."),
    max_repos_per_user: int = Query(
        1, description="The maximum number of repositories per user."
    ),
    db: AsyncSession = Depends(get_db),
    text_process_service: TextProcessService = Depends(get_text_process_service),
    embedding_service: EmbeddingService = Depends(get_embedding_service),
    extraction_service: ExtractionService = Depends(get_extraction_service),
):
    logger.info("------------  Starting data ingestion process")
    try:
        logger.info(" ------------ Extracting data")
        all_data = await extraction_service.extract_data(
            location, max_users, max_repos_per_user
        )

        logger.info(" ------------ Filtering new READMEs")
        existing_repos = await db.execute(select(GitRepository.repo_name))
        logger.info(f"#### {existing_repos.scalars().all()}")
        existing_names = {repo.repo_name for repo in existing_repos.scalars().all()}
        logger.info(f"#### {existing_names}")
        new_data = [
            data for data in all_data if data["repo_name"] not in existing_names
        ]

        logger.info(" ------------ Processing READMEs")
        processed_readmes = [
            text_process_service.process_text(data["readme"]) for data in new_data
        ]

        logger.info(" ------------ Generating embeddings")
        # embeddings = [
        #     embedding_service.generate_embeddings(readme)
        #     for readme in processed_readmes
        # ]

        # embeddings = await asyncio.gather(
        #     *(
        #         embedding_service.generate_embeddings(readme)
        #         for readme in processed_readmes
        #     )
        # )
        embeddings = []
        for readme in processed_readmes:
            embedding = embedding_service.generate_embeddings(readme)
            embeddings.append(embedding)

        logger.info("Loading new data into database")
        github_crud = GitHubCRUD()
        logger.info("Creating new users")
        for data, embedding in zip(new_data, embeddings):

            user = await github_crud.create_git_user(
                db,
                {
                    "username": data["username"],
                    "location": location,
                },
            )
            logger.info(f"Creating repository: {data['repo_name']}")
            await github_crud.create_git_repository(
                db,
                {
                    "username": user.username,
                    "repo_name": data["repo_name"],
                    "readme_raw": data["readme"],
                    "readme_cleaned": processed_readmes[new_data.index(data)],
                    "readme_embedding": embedding,
                },
            )
        logger.info("Data ingestion completed successfully")
        return {"status": "Data ingestion successful"}
    except Exception as e:
        logger.error(f"Data ingestion process failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))
