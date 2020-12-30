FROM python:3.9

# Install poetry
RUN pip install poetry

# Configure Poetry for deployment: no interaction, install packages directly (not in virtualenv)
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false

# Expose our webapp port
EXPOSE 8000

# Launch our webapp when Docker container starts
ENTRYPOINT ["./docker-entrypoint.sh"]

# Setup our webapp working directory
WORKDIR /app

# Install our webapp, in production mode
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-dev

# Copy our webapp source code
COPY . /app
