FROM python:3.13-slim-bookworm

ENV FLASK_APP_USER="flask_app"
ENV FLASK_APP_HOME="/usr/local/$FLASK_APP_USER"

USER root

RUN useradd --shell /bin/bash -d "$FLASK_APP_HOME" -m -u 1001 "$FLASK_APP_USER"

COPY ./requirements.txt "$FLASK_APP_HOME"
COPY ./scripts/entrypoint.sh "$FLASK_APP_HOME"

RUN pip3 install -r "$FLASK_APP_HOME/requirements.txt"

RUN chmod +x "$FLASK_APP_HOME/entrypoint.sh"
RUN chown -R "$FLASK_APP_USER": "$FLASK_APP_HOME"

EXPOSE 8080

USER $FLASK_APP_USER

WORKDIR "$FLASK_APP_HOME"

ENTRYPOINT ["./entrypoint.sh"]