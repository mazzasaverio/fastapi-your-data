# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY requirements.txt /code/

# Install necessary dependencies
RUN pip install sentence-transformers

# Pre-download the model to the image
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY ./app /code/app

ENV PYTHONPATH=/code
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
