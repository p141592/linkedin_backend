FROM python:3.6-alpine as builder

RUN apk update && apk add build-base postgresql-dev libffi-dev python-dev zlib-dev jpeg-dev
RUN mkdir /tmp/install

COPY ./pip /tmp/requirements/
RUN pip install --prefix=/tmp/install -r /tmp/requirements/prod.pip
###

FROM python:3.6-alpine
RUN addgroup -S www-data && adduser -S www-data -G root
RUN apk update && apk add postgresql-dev libffi-dev zlib-dev jpeg-dev bash zeromq
COPY --from=builder /tmp/install /usr/local
###

COPY entrypoint.sh /k0d/k0d
RUN chmod -R 755 /k0d/
ENV PATH /k0d:$PATH
###

RUN mkdir -p /var/www/media/ && chown -R www-data:www-data /var/www/media/
RUN mkdir -p /var/www/static/ && chown -R www-data:www-data /var/www/static/
###

ENV DJANGO_SETTINGS_MODULE settings.prod
ENV PYTHONPATH /opt/application/
ENV APP_MIGRATE 1
ENV APP_COLLECTSTATIC 1
ENV APP_STATIC_ROOT /var/www/static/
ENV APP_MEDIA_ROOT /var/www/media/
##

COPY src /opt/application/

WORKDIR /opt/application

USER www-data

EXPOSE 8000

CMD k0d start
