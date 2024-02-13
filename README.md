# FastAPI Your Data

I am starting this project with the idea of continuously building and improving a methodology and basic structure that allows for the effective organization and historical storage of data of interest. This includes managing the data and having it ready for use in various projects.

The concept is to let myself be guided by the following principles (subjective) and see if I can find a methodology that works for me (though I hope it will be inspirational or at least useful to others).

- In the future, the real competitive difference in many contexts and from various perspectives will be the ability to have quality, up-to-date data. This will be more important than having a better model than others because, for modeling, one will likely start with pre-trained models from large companies that can afford to stay at the cutting edge. There will be RAG, fine-tuning, etc., but the real competitive difference will be the quality of the data and the ability to put these models into production.
- Finding an effective and cost-effective system that is robust from a production standpoint, not just development, so that individuals can organize and keep their data up-to-date for various projects and have "a guide" to scale these projects in the future.
- The ideal world would be to build a "template" along with documentation and best practices to scale while keeping costs lower than profits, trying to keep track of all mistakes and why of some decisions.
- This project is an excuse to study, experiment, practice, and improve all the topics I am interested in improving as a data engineer and backend engineer. It's about building a methodology and a system that allows me to always have access to all the historical data and have it ready for any current or future idea or project.
- Having documentation as updated as possible on the theory, practice, and specific choices for this repository, starting with the fundamentals and experimenting through various tools, frameworks, and tools.

Certainly, to move in this direction, I will also start other parallel repositories to cover different parts of this system (including ETL processes or frontend parts), but the heart of this direction will be this repository.

## Current Progress

- **Database Connection**: Initiated with a basic connection to a PostgreSQL database utilizing SQLAlchemy's ORM.
- **Design Philosophy**: The design I am adopting involves having a structure where the app will be supplemented with other independent modules. These modules will be managed and mounted by a main.py in the root, which, through an API gateway, will redirect various calls.
- **Data Module Focus**: Presently concentrating on a single module, which will correspond to a specific family or category of data. Each data category will have its own dedicated database with a unique table structure.
- **Architecture**: The design includes a models layer and a repository layer for database interactions. The API layer, with its various routes, forms the final layer of the architecture.

## Environment Setup

1. Create a **.env** file in the root folder.
2. Copy the contents from **.env.example**.
3. Modify as needed for your configuration.

## Local Backend Development

Execute in terminal:

```
docker-compose -f docker-compose-dev.yml up --build
```

## Deploying to a Cloud Instance (e.g., GCP Compute Engine)

1. Log in to Docker:

   ```
   docker login
   ```

2. Pull the Docker image:

   ```
   docker pull inter92/fastapi-service:master
   ```

3. Run the container:

   ```
   docker run -p 8000:8000 --network="host" -e DB_HOST=${DB_HOST}   -e DB_PORT=${DB_PORT}  -e DB_NAME=${DB_NAME}   -e DB_PASS=${DB_PASS}  -e DB_USER=${DB_USER}   -e API_KEY=${API_KEY}  inter92/fastapi-service:master
   ```

## Alembic Migrations

To automatically generate a migration script based on your model changes, run:

alembic revision --autogenerate -m "Create tables"

This command compares your database schema with your SQLAlchemy models and creates a migration script.

To apply the generated migrations to your database, execute:

alembic upgrade head
This command runs the migration script(s) against your database, upgrading it to the latest version.

## Additional Resources

- Infrastructure details using Terraform: [Terraform GCP Repository](https://github.com/mazzasaverio/terraform-gcp)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Useful Docker Commands

To remove all Docker containers:

1. Stop all running containers:

   ```
   docker stop $(docker ps -q)
   ```

2. Remove all containers:

   ```
   docker rm $(docker ps -a -q)
   ```

## SSH Warning: Remote Host Identification Changed

This warning indicates a change in the server's SSH fingerprint, potentially signaling a security risk.

- To resolve, if the change is legitimate, remove the old key:

  ```
  ssh-keygen -f "/home/user/.ssh/known_hosts" -R "server_ip"
  ```

- If unsure, investigate or contact the server administrator.

## FastAPI App Deployment

1. Build the Docker image:

   ```
   docker build -t fastapi-app .
   ```

2. Run the container:

   ```
   docker run -d --name fastapi_container -p 8000:8000 \
   --network="host" \
   --env-file ./.env \
   fastapi-app
   ```

3. Docker commands to manage the container:

   ```
   docker logs fastapi_container
   docker stop fastapi_container
   docker rm fastapi_container
   ```

<!-- START_SECTION:under-review -->

## Repositories Under Review

|                                      Repository                                      | Stars | Forks | Last Updated |                                       About                                        |
| :----------------------------------------------------------------------------------: | :---: | :---: | :----------: | :--------------------------------------------------------------------------------: |
|            [JumpStart](https://github.com/Aeternalis-Ingenium/JumpStart)             |  46   |   7   |  2024-02-06  | A lean web application template with FastAPI, Uvicorn, Docker, and GitHub Actions. |
| [instagraph-nextjs-fastapi](https://github.com/waseemhnyc/instagraph-nextjs-fastapi) |  67   |  11   |  2024-02-03  |        Generate knowledge graphs. Inspired by @yoheinakajima instagraph.ai         |
|      [video-2-text](https://github.com/XamHans/video-2-text?tab=readme-ov-file)      |  53   |  17   |  2024-02-02  |                   Video2Text - Easily convert your video to text                   |

<!-- END_SECTION:under-review -->
<!-- START_SECTION:reference-inspiration -->

## Reference and Inspiration

|                                          Repository                                           | Stars | Forks | Last Updated |                                                                                About                                                                                |
| :-------------------------------------------------------------------------------------------: | :---: | :---: | :----------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [fastapi-alembic-sqlmodel-async](https://github.com/jonra1993/fastapi-alembic-sqlmodel-async) |  660  |  114  |  2024-02-06  | This is a project template which uses FastAPI, Alembic and async SQLModel as ORM. It shows a complete async CRUD using authentication and role base access control. |
|                       [fastcrud](https://github.com/igorbenav/fastcrud)                       |  242  |  12   |  2024-02-06  |                      FastCRUD is a Python package for FastAPI, offering robust async CRUD operations and flexible endpoint creation utilities.                      |

<!-- END_SECTION:reference-inspiration -->
