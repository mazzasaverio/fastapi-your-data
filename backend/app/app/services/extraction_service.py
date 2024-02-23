import httpx
from loguru import logger
from typing import List, Dict
import requests


class GitHubAPI:
    """
    GitHub API wrapper to fetch user and repository data.
    """

    def __init__(self, access_token: str):
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"token {access_token}"}
        logger.debug("GitHubAPI initialized with token.")

    def get_user_repos(self, username: str, max_repos: int) -> List[Dict]:
        """
        Fetch repositories for a given GitHub username synchronously.
        """
        repos = []
        page = 1
        while len(repos) < max_repos:
            url = f"{self.base_url}/users/{username}/repos?per_page=100&page={page}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            page_repos = response.json()
            repos.extend(page_repos)
            if len(page_repos) < 100:
                break  # No more repos to fetch
            page += 1
        logger.info(f"Fetched {len(repos)} repos for user: {username}")
        return repos[:max_repos]

    def get_readme(self, owner: str, repo: str) -> str:
        """
        Fetch the README for a given repository synchronously.
        """
        url = f"{self.base_url}/repos/{owner}/{repo}/readme"

        logger.debug(f"Fetching README for repo: {repo} of owner: {owner}")
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            readme_data = response.json()
            readme_content = readme_data.get("content", "")
            logger.debug("README fetched successfully.")
            return readme_content
        logger.warning("README not found.")
        return ""


class ExtractionService:
    """
    Service to extract GitHub users and their repositories based on location.
    """

    def __init__(self, access_token: str):
        self.github_api = GitHubAPI(access_token)
        logger.info("ExtractionService initialized.")

    def fetch_users_by_location(self, location: str, max_users: int) -> List[Dict]:
        """
        Fetch GitHub users based on location.
        """
        url = f"{self.github_api.base_url}/search/users?q=location:{location}&per_page={max_users}"
        logger.info(f"Fetching users by location: {location}")
        response = requests.get(url, headers=self.github_api.headers)
        response.raise_for_status()
        users_data = response.json().get("items", [])
        logger.info(f"Fetched {len(users_data)} users from location: {location}")
        return users_data

    def extract_data(
        self, location: str, max_users: int, max_repos_per_user: int
    ) -> List[Dict]:
        """
        Extract GitHub user and repository data based on location.
        """
        users = self.fetch_users_by_location(location, max_users)
        all_data = []
        logger.info(f"Extracting data for {len(users)} users.")
        for user in users:
            repos = self.github_api.get_user_repos(user["login"], max_repos_per_user)
            for repo in repos:
                readme = self.github_api.get_readme(user["login"], repo["name"])
                all_data.append(
                    {
                        "username": user["login"],
                        "repo_name": repo["name"],
                        "readme": readme,
                    }
                )
        logger.info("Data extraction complete.")
        return all_data


# class ExtractionService:
#     """
#     Service to extract GitHub users and their repositories based on location.
#     """

#     def __init__(self, access_token: str):
#         self.github_api = GitHubAPI(access_token)
#         logger.info("ExtractionService initialized.")

#     async def fetch_users_by_location(
#         self, location: str, max_users: int
#     ) -> List[Dict]:
#         """
#         Fetch GitHub users based on location.
#         """
#         url = f"{self.github_api.base_url}/search/users?q=location:{location}&per_page={max_users}"
#         logger.info(f"Fetching users by location: {location}")
#         async with httpx.AsyncClient() as client:
#             response = await client.get(url, headers=self.github_api.headers)
#             response.raise_for_status()
#             users_data = response.json().get("items", [])
#             logger.info(f"Fetched {len(users_data)} users from location: {location}")
#             return users_data

#     async def extract_data(
#         self, location: str, max_users: int, max_repos_per_user: int
#     ) -> List[Dict]:
#         """
#         Extract GitHub user and repository data based on location.
#         """
#         users = await self.fetch_users_by_location(location, max_users)
#         all_data = []
#         logger.info(f"Extracting data for {len(users)} users.")
#         for user in users:
#             repos = await self.github_api.get_user_repos(
#                 user["login"], max_repos_per_user
#             )
#             for repo in repos:
#                 readme = await self.github_api.get_readme(user["login"], repo["name"])
#                 all_data.append(
#                     {
#                         "username": user["login"],
#                         "repo_name": repo["name"],
#                         "readme": readme,
#                     }
#                 )
#         logger.info("Data extraction complete.")
#         return all_data
