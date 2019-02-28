# Подключение ENV переменных
# Монтирование статики
# Положить nginx конфиг и ssl в место назначения

FROM python:3.6

COPY ./pip /tmp/requirements/
RUN pip install -r /tmp/requirements/dev.pip

###

COPY entrypoint.sh /k0d/k0d
RUN chmod -R 755 /k0d/
ENV PATH /k0d:$PATH
###

RUN mkdir -p /var/www/media/ && chown -R www-data /var/www/media/
RUN mkdir -p /var/www/static/ && chown -R www-data /var/www/static/
###

ENV DJANGO_SETTINGS_MODULE settings.dev
ENV PYTHONPATH /opt/application/
ENV APP_MIGRATE 1
ENV APP_COLLECTSTATIC 1
ENV APP_CREATE_SUPERUSER 1
ENV APP_DEBUG 1
##

COPY src /opt/application/
WORKDIR /opt/application
###

VOLUME /var/www/media/
VOLUME /var/www/static/

EXPOSE 8000

CMD k0d start
