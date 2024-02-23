from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dependencies import get_db, get_embedding_service, get_similarity_service
from app.services.embedding_service import EmbeddingService
from app.services.similarity_service import SimilarityService
from loguru import logger

router = APIRouter()


@router.post("/calculate_similarity")
async def calculate_similarity(
    input_text: str = Body(..., embed=True),
    db: AsyncSession = Depends(get_db),
    embedding_service: EmbeddingService = Depends(get_embedding_service),
    similarity_service: SimilarityService = Depends(get_similarity_service),
):
    """
    Calculate similarity scores between the input text and embeddings in the `git_repositories_n2` table.

    Args:
        input_text (str): The input text from the user.
        db (AsyncSession): Dependency injection for the database session.
        embedding_service (EmbeddingService): Dependency injection for the embedding service.
        similarity_service (SimilarityService): Dependency injection for the similarity service.

    Returns:
        A list of repositories and their similarity scores with the input text.
    """
    # Generate embedding for the input text
    input_embedding = embedding_service.generate_embeddings(input_text)
    logger.info(f"Input embedding: {input_embedding}")

    # Calculate similarity scores
    similarities = await similarity_service.calculate_similarity(db, input_embedding)

    logger.info(f"Similarities: {similarities}")

    # Format and return the results
    return {
        "similarities": [
            {"repo_name": name, "score": score} for name, score in similarities
        ]
    }
