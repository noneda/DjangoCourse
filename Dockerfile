FROM python:3.11-alpine

LABEL maintainer="DjangoCourse"
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./src /app

WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt \
    && rm -rf /tmp \
    && adduser \
        --disabled-password \
        --no-create-home \
        django-user


ENV path="/py/bin:$PATH"

USER django-user
