# FastAPI Your Data

This project aims to serve as a template for developing a FastAPI backend. It is designed for experimenting with various aspects such as costs, functionality, and performance. The ultimate goal is to facilitate the creation of a customizable backend setup that can be efficiently deployed on the cloud, allowing for scalable and modular development, and enabling the exposure of datasets.

## Current Progress

- **Database Connection**: Initiated with a basic connection to a PostgreSQL database utilizing SQLAlchemy's ORM.
- **Design Philosophy**: The design I am adopting involves having a structure where the app will be supplemented with other independent modules. These modules will be managed and mounted by a main.py in the root, which, through an API gateway, will redirect various calls.
- **Data Module Focus**: Presently concentrating on a single module, which will correspond to a specific family or category of data. Each data category will have its own dedicated database with a unique table structure.
- **Architecture**: The design includes a models layer and a repository layer for database interactions. The API layer, with its various routes, forms the final layer of the architecture.

## Set environment variables

Create an **.env** file on root folder and copy the content from **.env.example**. Feel free to change it according to your own configuration.

## Se si vuole runnare il backend in dev locale

docker-compose -f docker-compose-dev.yml up --build

## Per eseguire l'immagine su un istanza per esempio una compute engine gcp

docker login

docker pull inter92/fastapi-service

## Alembic migrations

## Inspiration and References

- [fastapi-alembic-sqlmodel-async](https://github.com/jonra1993/fastapi-alembic-sqlmodel-async).
- [fastcrud](https://github.com/igorbenav/fastcrud)
- [fullstack-flask-app](https://github.com/FrancescoXX/fullstack-flask-app)

## TODO List:

- [x] Transition to asynchronous interactions with the database.
- [x] Connect a frontend in Next.js.

## TODO Ideas to test:

## Additional Resources

- For those interested in the infrastructure aspect, the Terraform code for various services being used in this project can be found here: [Terraform GCP Repository](https://github.com/mazzasaverio/terraform-gcp)

## Interesting, to be reviewed

- [video-2-text](https://github.com/XamHans/video-2-text?tab=readme-ov-file)
- [instagraph-nextjs-fastapi](https://github.com/waseemhnyc/instagraph-nextjs-fastapi)

## Contributing

Contributions to the project are welcome! Feel free to open an issue or submit a pull request.
