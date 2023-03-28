#!/bin/bash

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py migrate --noinput

echo "Starting server"
gunicorn hello_docker.wsgi:application --bind 0.0.0.0:8000