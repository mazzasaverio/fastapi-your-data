# FastAPI Your Data

I am starting this project with the goal of continuously learning, building, and enhancing a methodology and foundational structure to effectively archive data of interest and utilize it in production. The idea is to maintain a sufficiently general structure and use this repository as a laboratory to understand basics, concepts, frameworks and to have a starting template for various configurations.

## Tech stack

- Python 3.10 with fastapi and SQLAlchemy
- Local Postgres with pgvector extension

## Quickstart

## Current Features

## Metodology

The concept is to let myself be guided by the following principles (subjective) and see if I can find a methodology that works for me (though I hope it will be inspirational or at least useful to others).

- In the future, the real competitive difference in many contexts and from various perspectives will be the ability to have quality, up-to-date data. This will be more important than having a better model than others because, for modeling, one will likely start with pre-trained models from large companies that can afford to stay at the cutting edge. There will be RAG, fine-tuning, etc., but the real competitive difference will be the quality of the data and the ability to put these models into production.
- Finding an effective and cost-effective system that is robust from a production standpoint, not just development, so that individuals can organize and keep their data up-to-date for various projects and have "a guide" to scale these projects in the future.
- The ideal world would be to build a "template" along with documentation and best practices to scale while keeping costs lower than profits, trying to keep track of all mistakes and why of some decisions.
- This project is an excuse to study, experiment, practice, and improve all the topics I am interested in improving as a data engineer and backend engineer. It's about building a methodology and a system that allows me to always have access to all the historical data and have it ready for any current or future idea or project.
- Having documentation as updated as possible on the theory, practice, and specific choices for this repository, starting with the fundamentals and experimenting through various tools, frameworks, and tools.

### Design Philosophy

The design strategy incorporates a framework where the application is enhanced with several independent modules. These modules are orchestrated and integrated by `main.py` at the root level, which routes various requests through an API gateway.

Although it might seem overwhelming at first, adopting a monorepo accelerates the design and learning process. Nonetheless, I strive to keep everything modular to facilitate the structuring of microservices or the segregation of different components into separate repositories when scaling becomes necessary in the future.

### Database Connection

The goal is to start as agnostically as possible by using SQLAlchemy as the ORM and exploring the best ODM options for unstructured data.

Currently, I am beginning with PostgreSQL, leveraging the pgvector extension for embedding-related data.

## In Progress

- ETL processes to populate and maintain the database up-to-date.

## Future Features

## Environment Setup

1. Create a **.env** file in the root folder.
2. Copy the contents from **.env.example**.
3. Modify as needed for your configuration.

## Local Backend Development

Execute in terminal:

```
docker-compose -f docker-compose-dev.yml up --build
```

## Deploying to a Cloud Instance (e.g., GCP Compute Engine

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
   docker run -p 8080:8080 --network="host" -e DB_HOST=${DB_HOST}   -e DB_PORT=${DB_PORT}  -e DB_NAME=${DB_NAME}   -e DB_PASS=${DB_PASS}  -e DB_USER=${DB_USER}   -e API_KEY=${API_KEY}  inter92/fastapi-service:master
   ```

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
   docker run -d --name fastapi_container -p 8080:8080 \
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

## References and Inspirations

### Github

- [fastapi-alembic-sqlmodel-async](https://github.com/jonra1993/fastapi-alembic-sqlmodel-async): A project integrating FastAPI with Alembic and SQLModel for asynchronous database operations.
- [fastcrud](https://github.com/igorbenav/fastcrud): A library for simplifying CRUD operations in FastAPI.
- [agentkit](https://github.com/BCG-X-Official/agentkit): A toolkit for building intelligent agents.
- [fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices)

### Books

- [Building Python Microservices with FastAPI](https://amzn.to/3SZvdFk)

## Watchlist Repositories

- [JumpStart](https://github.com/Aeternalis-Ingenium/JumpStart): A starter template for new projects.
- [instagraph-nextjs-fastapi](https://github.com/waseemhnyc/instagraph-nextjs-fastapi): An integration of Next.js with FastAPI for building Instagram-like applications.
- [video-2-text](https://github.com/XamHans/video-2-text?tab=readme-ov-file): A project focused on converting video content to text.
