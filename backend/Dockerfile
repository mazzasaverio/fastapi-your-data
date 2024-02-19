# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /code/app

ENV PYTHONPATH=/code
EXPOSE 8080

CMD ["conda", "run", "-n", "fastapi-your-data", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]