import os

from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API')

e = os.environ.get

urlpatterns = [
    url(r'^swagger/', schema_view),
    url(r'^v1/core/', include('core.urls')),
    url(r'^admin/', admin.site.urls),
] + staticfiles_urlpatterns()
