# syntax=docker/dockerfile:1
FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./requirements /code/requirements
RUN pip install -r /code/requirements/dev.txt

COPY ./src /code/src
COPY ./services /code/services
COPY ./environments/default.env /code/environments/default.env

COPY setup.cfg /code/
COPY Makefile /code/
COPY README.md /code/
COPY ./infra/api-entrypoint.sh /code/

RUN mkdir /app
RUN chmod +x /code/api-entrypoint.sh

ENTRYPOINT [ "bash", "/code/api-entrypoint.sh" ]