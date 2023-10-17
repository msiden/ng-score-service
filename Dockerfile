FROM python:3.11-slim-buster as builder

COPY ./src/requirements.txt /tmp/requirements.txt
COPY ./src /usr/src/app

RUN pip install -r /tmp/requirements.txt

WORKDIR /usr/src/app/score-service

ARG NGDB_ENV
ARG NGDB_PASSWORD
ARG NGDB_URL
ENV NGDB_ENV=$NGDB_ENV
ENV NGDB_PASSWORD=$NGDB_PASSWORD
ENV NGDB_URL=$NGDB_URL

EXPOSE 8081

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8081", "app:app()"]
