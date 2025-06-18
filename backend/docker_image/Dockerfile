FROM python:3.13-bookworm

ENV FLASK_APP_USER="flask_app"
ENV FLASK_APP_USER_HOME="/usr/local/$FLASK_APP_USER/"

USER root

RUN useradd --shell /bin/bash -d "$FLASK_APP_USER_HOME" -m -u 1001 "$FLASK_APP_USER"

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

RUN chown -R "$FLASK_APP_USER": "$FLASK_APP_USER_HOME"

USER "$FLASK_APP_USER"

WORKDIR "$FLASK_APP_USER_HOME"
