import requests
from app.api.v1.endpoints.utils.github_api import GitHubAPI
from tqdm import tqdm
from loguru import logger


def fetch_users_by_location(location, max_users, access_token):
    users = []
    url = f"https://api.github.com/search/users?q=location:{location}&per_page={max_users}"
    headers = {"Authorization": f"token {access_token}"}

    try:
        response = requests.get(url, headers=headers, timeout=70).json()
        users.extend(response.get("items", []))
        logger.info(
            f"Successfully fetched {len(users)} users from location: {location}"
        )
    except Exception as e:
        logger.error(f"Failed to fetch users from location: {location}. Error: {e}")

    return users


def fetch_repo_readmes(users, max_repos_per_user, access_token):
    github_api = GitHubAPI(access_token)
    all_readmes = []
    for user in tqdm(users, desc="Fetching repositories"):
        repos = github_api.get_user_repos(user["login"], max_repos=max_repos_per_user)
        for repo in repos:
            readme = github_api.get_readme(repo)
            if readme:
                all_readmes.append(
                    {
                        "username": user["login"],
                        "repo_name": repo["name"],
                        "readme_text": readme,
                    }
                )
    return all_readmes
