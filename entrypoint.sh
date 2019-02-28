#!/usr/bin/env bash

set -e

APP_GUNICORN_USE=${APP_GUNICORN_USE:-"wsgi:application"}
APP_GUNICORN_MAX_REQUESTS=${APP_GUNICORN_MAX_REQUESTS:-"1000"}

APP_WORKERS_DEFAULT=$(nproc)
APP_WORKERS=${APP_WORKERS:-$APP_WORKERS_DEFAULT}

APP_HOST=${APP_HOST:-"0.0.0.0"}
APP_PORT=${APP_PORT:-"8000"}

if ! [ -z "$APP_MIGRATE" ]; then
  django-admin makemigrations --noinput
  django-admin migrate --noinput
fi

if ! [ -z "$APP_COLLECTSTATIC" ]; then
  django-admin collectstatic --noinput
fi

if ! [ -z "$APP_COMMAND" ]; then
  django-admin $APP_COMMAND
  exit 0;
fi

if ! [ -z "$APP_CREATE_SUPERUSER" ]; then
  echo "from django.contrib.auth import get_user_model; bool(get_user_model().objects.filter(username='admin').count()) or get_user_model().objects.create_superuser('admin', 'admin@example.com', 'admin')" | django-admin shell
fi

if ! [ -z "$APP_DEBUG" ]; then
  django-admin runserver ${APP_HOST}:${APP_PORT}
else
  gunicorn -b ${APP_HOST}:${APP_PORT} --capture-output --max-requests $APP_GUNICORN_MAX_REQUESTS -w $APP_WORKERS -k gevent $APP_GUNICORN_USE
fi
