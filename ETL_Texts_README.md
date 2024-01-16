
# ETL-Texts

## Overview
ETL-Texts is a robust and flexible pipeline designed for extracting, translating, cleaning, and transforming text files into embeddings, making them readily usable for training or inference in various natural language processing models. It operates on the principle that each step in the process requires an input path and an output path, allowing for independent execution or a sequential flow through the pipeline.

## Features
- **Text Extraction**: Utilizes the `unstructured` package to extract text. (See `src/services/text_extractor.py`)
- **Text Translation**: Employs a multilingual model for optional text translation. (See `src/services/text_translator.py`)
- **Text Cleaning**: Aggregates and cleans text according to specific requirements. (Currently under development, see `src/services/text_cleaner.py`)
- **Text Embedding**: Processes embedding as per user-defined requirements and saves it either in storage or in a vector database. (Currently under development, see `src/services/text_embeddings.py`)

The system is built on the principle that a file will be processed only if it hasn't been processed previously, which is determined by checking the destination path. Outputs are consistently formatted in JSON to facilitate flexible manipulation and ingestion stages, irrespective of the source or destination.

## Configuration
Input and output paths are set through the `.env` file (refer to `.env.example`, which should be renamed to `.env`).

## Roadmap
- Parallelization and containerization of the process for enhanced performance.
- Automation of the process by orchestrating an event-driven pipeline capable of leveraging serverless computing depending on the scale and processing time requirements.
- Provisioning for varied inputs and outputs to facilitate choice or alternation between data lakes, SQL databases, or NoSQL databases.

## Installation
(Instructions on how to install and set up the pipeline)

## Usage
(Instructions on how to use the pipeline, including examples)

## Contributing
(Guidelines for contributing to the project)

## License
(Information about the project's license)
