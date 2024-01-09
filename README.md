# data-FastAPI

## Overview

This repository contains the foundational code for a FastAPI application that connects to a SQL database using SQLModel. The goal is to deploy this API on Google Cloud Platform (GCP) and utilize Cloud SQL as the database service.

## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repo-name
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Local Development

1. Start your local development server:

   ```bash
   uvicorn main:app --reload
   ```

2. Access the API at `http://localhost:8000`.

### Database Configuration

- Configure your local and Cloud SQL database credentials in the `.env` file.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request for any enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
