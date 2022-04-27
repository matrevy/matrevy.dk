# Pull base image
FROM python:3.9

# Set work directory
WORKDIR /code

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements ./requirements
RUN pip install -r ./requirements/dev.txt

# Copy project
COPY . .
