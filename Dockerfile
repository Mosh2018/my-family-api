FROM python:3.9.6-slim-buster

MAINTAINER Mohamid

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev

RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install -r requirements.txt

RUN pip install psycopg2


RUN mkdir /app
WORKDIR /app
COPY ./app /app

