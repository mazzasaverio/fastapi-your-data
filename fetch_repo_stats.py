import requests
from loguru import logger
from datetime import datetime
from urllib.parse import urlparse


def get_repo_info_from_url(url):
    """
    Extracts the owner and repository name from a GitHub URL.
    """
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.strip("/").split("/")
    if len(path_parts) >= 2:
        return path_parts[-2], path_parts[-1]  # owner, repo
    else:
        return None, None


def get_repo_stats(url):
    """
    Fetches the statistics of a given GitHub repository URL.
    """
    owner, repo = get_repo_info_from_url(url)
    if not owner or not repo:
        logger.error(f"Invalid GitHub URL: {url}")
        return None, None, None, None

    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        last_updated = datetime.strptime(
            data["updated_at"], "%Y-%m-%dT%H:%M:%SZ"
        ).strftime("%Y-%m-%d")
        return (
            f"[{repo}]({url})",
            data["stargazers_count"],
            data["forks_count"],
            last_updated,
            data["description"],
        )
    else:
        logger.error(
            f"Failed to fetch data for {url}, status code: {response.status_code}"
        )
        return None, None, None, None, None


def generate_table_section(header, rows):
    """
    Generates a Markdown table section.
    """
    table = f"| {' | '.join(header)} |\n"
    table += "|" + ":-:|" * len(header) + "\n"  # Center align all columns
    for row in rows:
        # Make sure all elements are strings and skip rows with None values
        if all(element is not None for element in row):
            table += f"| {' | '.join(str(element) for element in row)} |\n"
    return table


def update_readme(under_review_repos, reference_inspiration_repos):
    """
    Updates the README file with separate tables for 'Under Review' and 'Reference and Inspiration' repositories.
    """
    # Section markers
    start_marker_under_review = "<!-- START_SECTION:under-review -->"
    end_marker_under_review = "<!-- END_SECTION:under-review -->"
    start_marker_reference_inspiration = "<!-- START_SECTION:reference-inspiration -->"
    end_marker_reference_inspiration = "<!-- END_SECTION:reference-inspiration -->"

    custom_heading_under_review = "## Repositories Under Review\n\n"
    custom_heading_reference_inspiration = "## Reference and Inspiration\n\n"

    under_review_stats = [get_repo_stats(url) for url in under_review_repos]
    under_review_stats.sort(
        key=lambda x: x[3] if x[3] is not None else "", reverse=True
    )

    reference_inspiration_stats = [
        get_repo_stats(url) for url in reference_inspiration_repos
    ]
    reference_inspiration_stats.sort(
        key=lambda x: x[3] if x[3] is not None else "", reverse=True
    )

    # Generate tables
    under_review_table = generate_table_section(
        ["Repository", "Stars", "Forks", "Last Updated", "About"],
        under_review_stats,
    )

    reference_inspiration_table = generate_table_section(
        ["Repository", "Stars", "Forks", "Last Updated", "About"],
        reference_inspiration_stats,
    )

    # Read the current README
    try:
        with open("README.md", "r") as file:
            readme_content = file.read()
    except FileNotFoundError:
        logger.error("README.md file not found.")
        return

    # Update the README
    updated_readme = readme_content
    sections = [
        (
            start_marker_under_review,
            end_marker_under_review,
            under_review_table,
            custom_heading_under_review,
        ),
        (
            start_marker_reference_inspiration,
            end_marker_reference_inspiration,
            reference_inspiration_table,
            custom_heading_reference_inspiration,
        ),
    ]

    for start_marker, end_marker, table, heading in sections:
        if start_marker in updated_readme and end_marker in updated_readme:
            section_start = updated_readme.find(start_marker)
            section_end = updated_readme.find(end_marker) + len(end_marker)
            updated_readme = (
                updated_readme[:section_start]
                + start_marker
                + "\n"
                + heading
                + table
                + end_marker
                + updated_readme[section_end:]
            )
        else:
            logger.info(
                f"Markers for {heading.strip()} not found, appending new table at the end."
            )
            updated_readme += "\n" + start_marker + "\n" + heading + table + end_marker

    # Write the updated README
    try:
        with open("README.md", "w") as file:
            file.write(updated_readme)
    except Exception as e:
        logger.error(f"Error writing to README.md: {e}")


reference_inspiration_repos = [
    "https://github.com/jonra1993/fastapi-alembic-sqlmodel-async",
    "https://github.com/igorbenav/fastcrud",
    "https://github.com/FrancescoXX/fullstack-flask-app",
    "https://github.com/zhanymkanov/fastapi-best-practices"
]

# Example usage
under_review_repos = [
    "https://github.com/XamHans/video-2-text?tab=readme-ov-file",
    "https://github.com/waseemhnyc/instagraph-nextjs-fastapi",
    "https://github.com/Aeternalis-Ingenium/JumpStart",
]

# Update the README
update_readme(under_review_repos, reference_inspiration_repos)
