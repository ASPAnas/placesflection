FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir -p $APP_HOME/staticfiles
WORKDIR $APP_HOME

RUN apt update && apt install python3-psycopg2

RUN pip3 install -U pipenv && pip3 install psycopg2-binary
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --pre

COPY . .

ENTRYPOINT ["/home/app/web/entrypoint.sh"]

