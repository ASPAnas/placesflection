# Places Remember

<p align="center">
<a href="https://github.com/ASPAnas/placesflection/actions/workflows/django.yml"><img alt="Django Tests" src="https://github.com/ASPAnas/placesflection/actions/workflows/django.yml/badge.svg"></a>
<a href="https://github.com/ASPAnas/placesflection/actions/workflows/black.yml"><img alt="Django Tests" src="https://github.com/ASPAnas/placesflection/actions/workflows/black.yml/badge.svg"></a>
<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Description

This application allows users to save and recall their memories. 

## Installation and usage

### Docker

Create an environment file with all the secrets and settings:

```
cp example.env .env && vi .env
```

To build service using docker use
```
docker-compose build
```

To run service run

```
docker-compose up -d
```

### No docker

To run the service without docker install all dependencies with pipenv:

```
cd placesflection
pipenv install
```

Then create an environment file with all the secrets and settings:

```
cp ../example.env .env && vi .env
```

To run service run

```
pipenv run ./manage.py runserver
```

## Tech overview

The application is written in [Python 3](https://github.com/python) and [Django](https://github.com/django/django), using [pipenv](https://github.com/pypa/pipenv) for package management and [black](https://github.com/psf/black) as a code formatter.

### Libraries

- django: web framework for the whole project.
- django-location-field: location field type and frontend.
- python-decouple: convenient configuration.
- social-auth-app-django: social auth.
- django-crispy-forms: to properly display forms with bootstrap.

#### Dev dependencies

- black: python code formatter.

## License

MIT

