FROM python:3.7.2
LABEL maintainer="I3L"

RUN mkdir /web
WORKDIR /web

# Env vars
ENV PYTHONUNBUFFERED 1

# Installing dependencies
RUN apt-get update && apt-get upgrade -y
RUN pip install -U pip setuptools
COPY requirements.txt /web/
RUN pip install -r /web/requirements.txt
ADD . /web/

# Django service
EXPOSE 8000