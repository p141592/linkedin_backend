import raven

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS.extend([
    'corsheaders',
    'raven.contrib.django.raven_compat'
])

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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

RAVEN_CONFIG = {
    'dsn': 'https://494cace15f37475382be04688a23c129:9fd08e81de3145538b9ee5233575639c@sentry.k0d.ru//3',
    'release': raven.fetch_git_sha(os.path.dirname(os.pardir))
}
