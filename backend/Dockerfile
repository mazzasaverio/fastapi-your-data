FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /code
# Install Poetry
RUN apt clean && apt update && apt install curl -y
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY app/pyproject.toml app/poetry.lock* /code/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --with dev --no-root ; else poetry install --no-root --no-dev ; fi"

ENV PYTHONPATH=/code
EXPOSE 8080

COPY ./app/app /code/app

CMD ["sh", "-c", "gunicorn -w 3 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:${PORT:-8080} --preload --log-level=debug --timeout 120"]
# CMD uvicorn app.main:app --port=${PORT:-8080} --host=0.0.0.0
# CMD ["uvicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]

