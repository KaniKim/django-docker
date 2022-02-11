FROM python:3.10.1

ENV PYTHONDONTWRITEVYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /django-docker

COPY Pipfile Pipfile.lock /django-docker/
COPY . /django-docker/

RUN pip install pipenv && pipenv install --system  && rm -rf /var/lib/apt/lists/* 

