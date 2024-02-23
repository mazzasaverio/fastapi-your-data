from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.github_model import GitUser, GitRepository
from app.crud.base_crud import BaseCRUD

from app.models.github_model import GitRepository, GitUser


from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.github_model import GitUser, GitRepository
from app.crud.base_crud import BaseCRUD
from sqlalchemy.exc import NoResultFound


class GitHubCRUD(BaseCRUD):
    def __init__(self):
        # Assuming you're working with GitRepository model here
        super().__init__(model=GitRepository)

    async def create_git_user(self, db: AsyncSession, user_data: dict) -> GitUser:
        try:
            # Attempt to fetch an existing user
            existing_user_query = await db.execute(
                select(GitUser).filter(GitUser.username == user_data["username"])
            )
            existing_user = existing_user_query.scalars().first()
        except NoResultFound:
            existing_user = None

        if existing_user is not None:
            # User already exists, skip creating a new user
            return existing_user

        # Create new GitUser instance
        user = GitUser(**user_data)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    async def create_git_repository(
        self, db: AsyncSession, repo_data: dict
    ) -> GitRepository:
        # Create new GitRepository instance
        repository = GitRepository(**repo_data)
        db.add(repository)
        await db.commit()
        await db.refresh(repository)
        return repository
