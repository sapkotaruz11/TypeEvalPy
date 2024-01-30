# Pull the Python base image
FROM python:3.10-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update \
    && apt-get -y install gcc

# Clone the repository
RUN git clone https://github.com/Instagram/MonkeyType.git


# Navigate into the cloned repository
WORKDIR /app/MonkeyType

RUN pip install --upgrade pip
RUN pip install .

COPY src /tmp/src

# Keep the container alive
CMD ["bash"]
