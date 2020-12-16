FROM ubuntu:20.04

# Install Python
RUN apt update
RUN apt install -y python3

# Install pip and other python installation tools
RUN apt install -y python3-pip
RUN python3 -m pip install --upgrade pip setuptools wheel poetry

# Copy our webapp source code
COPY . /app
WORKDIR /app

# Configure Poetry for deployment: no interaction, install packages directly (not in virtualenv)
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false

# Install our webapp, in production mode
RUN poetry install --no-dev

# Expose our webapp port
EXPOSE 8000

# Launch our webapp when Docker container starts
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
