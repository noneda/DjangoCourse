FROM python:3.11-alpine AS builder

LABEL maintainer="DjangoCourse"
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \
    build-base \
    python3-dev \
    musl-dev \
    libffi-dev \
    openssl-dev \
    postgresql-client \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    tiff-dev \
    tk-dev 

COPY ./requirements.txt /tmp/requirements.txt

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/requirements.txt

FROM python:3.11-alpine

LABEL maintainer="DjangoCourse"
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \
    postgresql-client \
    libffi \
    openssl \
    jpeg \
    zlib \
    freetype \
    lcms2 \
    tiff \
    tk

COPY --from=builder /py /py
COPY ./src /app

WORKDIR /app

RUN adduser -D -H django-user && \
    chown -R django-user:django-user /app /py

EXPOSE 8000

ENV PATH="/py/bin:$PATH"

USER django-user

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
