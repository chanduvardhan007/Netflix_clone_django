FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /Netflix_clone

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .







