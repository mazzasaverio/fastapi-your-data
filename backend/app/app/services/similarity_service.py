from typing import List, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text


class SimilarityService:
    def __init__(self):
        pass

    async def calculate_similarity(
        self, db: AsyncSession, user_embedding: List[float], top_k: int = 5
    ) -> List[Tuple[str, float]]:
        """
        Calculate similarity scores between a user's embedding and embeddings in the `git_repositories_n` table.

        Args:
            db (AsyncSession): The database session.
            user_embedding (List[float]): The embedding vector of the user's text.
            top_k (int): The number of top similar items to return.

        Returns:
            List[Tuple[str, float]]: A list of tuples containing the repository name and similarity score.
        """

        query = text(
            """
            SELECT repo_name, (readme_embedding <-> :user_embedding) AS similarity
            FROM git_repositories_n
            ORDER BY similarity ASC
            LIMIT :top_k;
        """
        )

        result = await db.execute(
            query, {"user_embedding": user_embedding, "top_k": top_k}
        )
        return result.fetchall()
