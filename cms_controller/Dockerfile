FROM python:3.10.12-alpine3.18

ENV PYTHONUNBUFFERED 1

COPY ./cms_controller/requirements.txt /requirements.txt
COPY ./cms_controller /cms_controller

WORKDIR /cms_controller
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --no-cache --virtual build-deps gcc musl-dev libffi pkgconf mariadb-dev && \
    apk add --no-cache mariadb-connector-c-dev && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app

ENV PATH="/py/bin:$PATH"

USER app
