# FastAPI Your Data

## Overview

This repository contains a modular and scalable backend application template using FastAPI and SQLAlchemy, focusing on data access by various users. Currently, the additional service layer is not considered, and operations are managed directly in the routes.

## Features

- **FastAPI Framework:** Building independent sub-applications within the main application.
- **SQLAlchemy for Database Management:** Effective handling of CRUD operations with SQLAlchemy.
- **Repository-Service Pattern:** Utilization of repository-service pattern for a structured approach to CRUD operations.

## Project Structure

The project is organized into several directories, each serving a specific purpose:

- `app`: Main application directory containing subdirectories for API routes, core functionalities, database configurations, repositories, schemas, and utilities.
- `config`: Contains configuration settings.
- `logs`: Log files are stored here.
- `Dockerfile` and `docker-compose.yml`: For containerization of the application.
- `requirements.txt`: Lists all the Python dependencies.

## Setting Up

To set up the project, follow these steps:

1. Install dependencies using `pip install -r requirements.txt`.
2. Set up the database using the provided scripts in the `app/database` directory.
3. Configure the `.env` file with the necessary environment variables.

## Running the Application

Launch the application using the following command:

```
uvicorn app.main:app --reload
```

## API Endpoints

The application provides several API endpoints under `/documents` and `/user` for handling documents and user-related operations, respectively.

## Security

The application uses hashed passwords for user authentication, ensuring enhanced security.

## Logging

Utilizes `loguru` for efficient logging throughout the application.

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file.

## Contribution

Contributions are welcome. Please fork the repository and submit a pull request with your changes.
