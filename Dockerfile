FROM python:3.9.6-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add libffi-dev
RUN apk add -u zlib-dev jpeg-dev gcc musl-dev
RUN python3 -m pip install --upgrade pip
RUN pip install psycopg2-binary
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

RUN mkdir /app
COPY ./ /app
WORKDIR /app