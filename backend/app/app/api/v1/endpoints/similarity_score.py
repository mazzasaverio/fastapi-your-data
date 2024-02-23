from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dependencies import get_db, get_embedding_service
from app.services.embedding_service import EmbeddingService
from loguru import logger
from app.crud.user_crud import UserSurveyCRUD
from sqlalchemy import text
from fastapi import HTTPException

router = APIRouter()


@router.post("/calculate_similarity")
async def calculate_similarity(
    user_id: str = Body(..., embed=True),
    input_text: str = Body(..., embed=True),
    db: AsyncSession = Depends(get_db),
    embedding_service: EmbeddingService = Depends(get_embedding_service),
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

    user_survey_crud = UserSurveyCRUD()

    logger.info(f"\n\nInput embedding: {len(input_embedding)}\n\n")

    await user_survey_crud.create_user_sarvey(
        db,
        {
            "user_name": "test",
            "survey_embedding": input_embedding,
        },
    )

    # Fetch the user's survey embedding
    query = text(
        """
        SELECT survey_embedding 
        FROM users_survey 
        WHERE user_id = :user_id;
    """
    )
    user_embedding_result = await db.execute(query, {"user_id": 1})
    user_embedding = user_embedding_result.scalar_one_or_none()

    if not user_embedding:
        raise HTTPException(status_code=404, detail="User survey embedding not found")

    # Use pgvector to calculate similarity with all readme_embedding
    similarity_query = text(
        """
        SELECT repo_name, (readme_embedding <-> :user_embedding) AS similarity 
        FROM git_repositories_n2 
        ORDER BY similarity ASC 
        LIMIT 5;
    """
    )
    similarities_result = await db.execute(
        similarity_query, {"user_embedding": user_embedding}
    )
    similarities = similarities_result.all()

    logger.info(f"Similarities: {similarities}")

    # Format and return the results
    return {
        "similarities": [
            {"repo_name": repo_name, "similarity": similarity}
            for repo_name, similarity in similarities
        ]
    }
