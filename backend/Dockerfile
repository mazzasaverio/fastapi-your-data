FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim
ENV PYTHONUNBUFFERED=1


# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY ./app /code/app
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/code
EXPOSE 8000

CMD uvicorn app.main:app --port=${PORT:-8000} --host=0.0.0.0
