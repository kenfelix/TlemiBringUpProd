#!/bin/bash

SUPER_EMAIL=${DJANGO_SUPER_EMAIL:-"emekaokafor08056@gmail.com"}
cd /app/

/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py createsuperuser --email $SUPER_EMAIL --noinput || true