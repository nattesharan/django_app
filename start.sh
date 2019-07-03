#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
gunicorn django_app.wsgi:application --bind=0.0.0.0:8000 --log-level info --access-logfile django_app.log --error-logfile app_errors.log --pid django_app.pid