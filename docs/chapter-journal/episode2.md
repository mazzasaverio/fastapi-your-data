## A step back and pgvector for … (FastAPI Your Data - Episode 2)

In this second episode of our project journey, I've made significant changes to the backend structure. The decision to focus primarily on a streamlined version means that what will eventually evolve into sub-applications are currently functioning as API routes. This approach is driven by the desire to first achieve a complete backend and frontend integration for a single sub-application. Despite not having a detailed plan at this stage, the myriad of topics needing exploration, study, and testing makes a rigid plan less practical. For instance, today, I spent more time than anticipated deciding on a vector database, eventually settling on pgvector for seamless integration with PostgreSQL. The significance of vector databases will become more apparent as we delve into modules involving natural language processing.

### GitHub Projects and Repos Search

One of the modules I'm excited to introduce and test involves searching GitHub projects and repositories based on criteria beyond the filters GitHub offers. I aim to enable searches based on project descriptions and README files, assigning scores based on my skills, goals, and interests. To this end, I've started with a basic script that fetches READMEs from GitHub users, extracts the content, and performs embedding, as shown below:

```python
import requests
from app.api.v1.endpoints.utils.github_api import GitHubAPI
from tqdm import tqdm
from loguru import logger

def fetch_users_by_location(location, max_users, access_token):
    users = []
    url = f"https://api.github.com/search/users?q=location:{location}&per_page={max_users}"
    headers = {"Authorization": f"token {access_token}"}

    try:
        response = requests.get(url, headers=headers).json()
        users.extend(response.get("items", []))
        logger.info(f"Successfully fetched {len(users)} users from location: {location}")
    except Exception as e:
        logger.error(f"Failed to fetch users from location: {location}. Error: {e}")

    return users
```

### GitHub Projects and Repos Search 2

This functionality is currently integrated as one of the endpoints, and I'm curious to see where it leads. My plan for tomorrow includes deploying everything on Cloud Run, though I must first address PostgreSQL initialization with pgvector, which requires enabling the extension—a task that is proving to be challenging directly through SQLAlchemy.

```python
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
```

### Cloud Deployment and SQL Challenges

For deploying on Cloud SQL in production through Cloud Run, I've encountered a workaround that involves using an SQL file for extension creation, which, while not the most elegant solution, serves our immediate needs. The importance of elegance is currently low on the priority list. I've found guidance for Cloud SQL integration with pgvector [here](https://cloud.google.com/blog/products/databases/using-pgvector-llms-and-langchain-with-google-cloud-databases), but further investigation is needed.

This episode marks another step forward in our project, blending backend development with vector databases and AI applications. Stay tuned for more updates as we continue to navigate through these exciting challenges and opportunities.
