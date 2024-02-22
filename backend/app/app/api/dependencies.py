from typing import AsyncGenerator
from fastapi import Depends, HTTPException, status
from fastapi.security.api_key import APIKeyHeader, APIKey
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings
from app.database.session import AsyncSessionFactory
from app.services.embedding_service import EmbeddingService, OpenAIEmbeddingService
from app.services.extraction_service import ExtractionService
from app.services.similarity_service import SimilarityService
from app.services.text_process_service import TextProcessService

api_key_header = APIKeyHeader(name="access_token")


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionFactory() as session:
        try:
            yield session
        finally:
            await session.close()


async def get_api_key(api_key_header: str = Depends(api_key_header)) -> APIKey:
    if api_key_header == settings.API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )


def get_embedding_service() -> EmbeddingService:
    return OpenAIEmbeddingService(api_key=settings.OPENAI_API_KEY)


def get_extraction_service() -> ExtractionService:
    return ExtractionService(access_token=settings.GITHUB_ACCESS_TOKEN)


def get_similarity_service() -> SimilarityService:
    return SimilarityService()


def get_text_process_service() -> TextProcessService:
    return TextProcessService()
