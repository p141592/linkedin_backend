from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

DATABASES = {
    'default': {
        'ENGINE': e("APP_DATABASES_ENGINE") or 'django.db.backends.postgresql',
        'NAME': e("APP_DB_NAME", 'postgres'),
        'USER': e("APP_DB_USER", 'postgres'),
        'PASSWORD': e("APP_DB_PASSWORD", 'postgres'),
        'HOST': e("APP_DB_HOST", 'localhost'),
        'PORT': int(e("APP_DB_PORT", 5432)),
        'CONN_MAX_AGE': 0  # was 3600 (1h)
    }
}

