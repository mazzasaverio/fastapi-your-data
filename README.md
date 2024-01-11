# FastAPI Your Data

## Introduction

This project aims to serve as a template for developing a FastAPI backend. It is designed for experimenting with various aspects such as costs, functionality, and performance. The ultimate goal is to facilitate the creation of a customizable backend setup that can be efficiently deployed on the cloud, allowing for scalable and modular development, and enabling the exposure of datasets.

## Current Progress

- **Database Connection**: Initiated with a basic connection to a PostgreSQL database utilizing SQLAlchemy's ORM.
- **Design Philosophy**: The design I am adopting involves having a structure where the app will be supplemented with other independent modules. These modules will be managed and mounted by a main.py in the root, which, through an API gateway, will redirect various calls.
- **Data Module Focus**: Presently concentrating on a single module, which will correspond to a specific family or category of data. Each data category will have its own dedicated database with a unique table structure.
- **Architecture**: The design includes a models layer and a repository layer for database interactions. The API layer, with its various routes, forms the final layer of the architecture.

## Technical Setup

- **CI/CD Integration**: Implemented a GitHub Actions workflow to prepare the deployment image.
- **Cloud Infrastructure**: Utilizing a Google Cloud Engine (GCE) instance and Cloud SQL for pipeline testing.

## Additional Resources

- For those interested in the infrastructure aspect, the Terraform code for various services being used in this project can be found here: [Terraform GCP Repository](https://github.com/mazzasaverio/terraform-gcp)

## Future Objectives

- Transition to asynchronous interactions with the database.
- Integration of a frontend using Next.js.

## Contributing

Contributions to the project are welcome! Feel free to open an issue or submit a pull request.
