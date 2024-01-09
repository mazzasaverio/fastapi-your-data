# Data-FastAPI

## Overview

`data-fastapi` is a comprehensive API designed for selling datasets. It supports various data types, both structured and unstructured, and offers modular, scalable access to data via an API key authentication system.

## Features

- Support for multiple databases: MongoDB, PostgreSQL, Redis, and a Data Lakehouse.
- Local and cloud deployment options for cost-effective development and scalability.
- API key authentication for secure and controlled data access.
- Modular structure for easy maintenance and scalability.

## Getting Started

aggiungi il tree della repo con la spiegazione di cosa rappresenta ogni cartella e file

### Prerequisites

- Docker
- Python 3.8+
- Terraform (for cloud deployment)

### Installation

Clone the repository:

```
git clone https://github.com/yourusername/data-fastapi.git
```

Install dependencies:

```
pip install -r requirements.txt
```

### Setting Up Local Environment

Copy `.env.sample` to create a `.env` file and adjust the variables to suit your local environment.

Run the Docker containers for databases:

```
docker-compose up -d
```

### Running the Application

Start the FastAPI application:

```
uvicorn app.main:app --reload
```

## API Documentation

Access the API documentation at `http://localhost:8000/docs`.

## Testing

Run tests using:

```
pytest
```

## Deployment

Refer to the `terraform/` directory for cloud deployment and `docker/` for containerization details.

## Contributing

Contributions, issues, and feature requests are welcome!

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - your@email.com
Project Link: https://github.com/yourusername/data-fastapi
