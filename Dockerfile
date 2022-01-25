FROM python:3.10.1

ENV PYTHONDONTWRITEVYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /docker-django

COPY Pipfile Pipfile.lock /docker-django/
COPY . /docker-django/