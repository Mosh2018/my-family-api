FROM python:3.9.6-slim-buster

MAINTAINER Mohamid

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN pip install psycopg2-binary


RUN mkdir /app
WORKDIR /app
COPY ./app /app

