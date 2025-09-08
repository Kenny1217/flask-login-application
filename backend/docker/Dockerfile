FROM python:3.13-slim-trixie

USER root

RUN useradd --shell /bin/bash -d /usr/local/flask_app -m -u 1001 flask_app

COPY ./requirements.txt /usr/local/flask_app

RUN pip3 install -r ./usr/local/flask_app/requirements.txt

EXPOSE 8080

USER flask_app

WORKDIR /usr/local/flask_app
