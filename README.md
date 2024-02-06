# FastAPI Your Data

This project aims to serve as a template for developing a FastAPI backend. It is designed for experimenting with various aspects such as costs, functionality, and performance. The ultimate goal is to facilitate the creation of a customizable backend setup that can be efficiently deployed on the cloud, allowing for scalable and modular development, and enabling the exposure of datasets.

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

## TODO List

- [x] Implement asynchronous database interactions.
- [x] Integrate a Next.js frontend.

## Testing Ideas

Further ideas are under consideration.

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

| Repository | Link | Stars | Forks | Last Updated |
|:-:|:-:|:-:|:-:|:-:|
| video-2-text | https://github.com/XamHans/video-2-text?tab=readme-ov-file | 53 | 17 | 2024-02-02T20:26:58Z |
| instagraph-nextjs-fastapi | https://github.com/waseemhnyc/instagraph-nextjs-fastapi | 67 | 11 | 2024-02-03T05:33:30Z |
<!-- END_SECTION:under-review -->
<!-- START_SECTION:reference-inspiration -->
## Reference and Inspiration

| Repository | Link | Stars | Forks | Last Updated |
|:-:|:-:|:-:|:-:|:-:|
| fastapi-alembic-sqlmodel-async | https://github.com/jonra1993/fastapi-alembic-sqlmodel-async | 660 | 114 | 2024-02-06T08:30:07Z |
| fastcrud | https://github.com/igorbenav/fastcrud | 241 | 12 | 2024-02-06T09:51:27Z |
| fullstack-flask-app | https://github.com/FrancescoXX/fullstack-flask-app | 4 | 3 | 2024-01-01T17:42:04Z |
<!-- END_SECTION:reference-inspiration -->