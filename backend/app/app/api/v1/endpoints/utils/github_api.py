import requests
import os


class GitHubAPI:
    def __init__(self, access_token):
        self.headers = {"Authorization": f"token {access_token}"}

    def get_user_repos(self, username, max_repos=10):
        repos = []
        page = 1
        while len(repos) < max_repos:
            url = (
                f"https://api.github.com/users/{username}/repos?per_page=30&page={page}"
            )
            response = requests.get(url, headers=self.headers).json()
            repos.extend(response)  # Accumulate repositories
            if not response:  # Exit the loop if the page has no repositories
                break
            page += 1
        return repos

    def get_readme(self, repo):
        contents_url = repo["contents_url"].replace("{+path}", "README.md")
        readme_response = requests.get(contents_url, headers=self.headers)
        if readme_response.status_code == 200:
            readme_data = readme_response.json()
            download_url = readme_data.get("download_url")
            if download_url:
                readme_text = requests.get(download_url).text
                return readme_text
        return None
