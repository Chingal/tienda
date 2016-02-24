# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from .email_info import *
#Configuracion de Correo
EMAIL_HOST          = EMAIL_HOST
EMAIL_PORT          = EMAIL_PORT
EMAIL_HOST_USER     = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_USE_TLS       = EMAIL_USE_TLS


from django.core.urlresolvers import reverse_lazy

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGOUT_URL = reverse_lazy('logout')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%o&f9u@p05&r*f^$mxqtn86atmuq(4-uqtf^(n-dtwtv5-66ix'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#Aplicaiones nativas de DJANGO
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
#Aplicaciones de terceros instaladas
THIRD_PARTY_APPS = (
    'south',
)
#Aplicaciones Locales Instaladas
LOCAL_APPS = (
    'tienda.apps.inicio',
    'tienda.apps.ventas',
)
# Application definition
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tienda.urls'

WSGI_APPLICATION = 'tienda.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'tienda.db'),
        }
}

# Internationalization
USE_I18N = True

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'tienda/media')

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
#STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['static'])
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'tienda/static'),
)
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'tienda/templates')
)
