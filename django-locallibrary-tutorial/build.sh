#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
export DJANGO_SUPERUSER_USERNAME=alumnodb
export DJANGO_SUPERUSER_PASSWORD=alumnodb
export DJANGO_SUPERUSER_EMAIL=admin@example.com
python manage.py createsuperuser --no-input
python populate_catalog2.py
