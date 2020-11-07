import os
from .std_settings import std_django as std_django
from .std_settings import std_site as std_site
from .std_settings import std_email as std_email
from .auth_settings import token_auth as auth
# from .auth_settings import oauth2 as auth

# Application definition
INSTALLED_APPS = (std_django._DJANGO_APPS + auth._AUTH_APPS
                  + std_site._SITE_APPS + std_site._TEST_APPS)

# Standard Django settings that rarely change
BASE_DIR = std_site.BASE_DIR
TEMPLATES = std_django.TEMPLATES
MIDDLEWARE = std_django.MIDDLEWARE
DATABASES = std_site.DATABASES

# Site settings that are subject to change
SITE_ID = std_site.SITE_ID
ROOT_URLCONF = std_site.ROOT_URLCONF
WSGI_APPLICATION = std_site.WSGI_APPLICATION
ALLOWED_HOSTS = std_site.ALLOWED_HOSTS
SECRET_KEY = std_site.SECRET_KEY
DEBUG = std_site.DEBUG

# Authentication Settings
_AUTH_MODE = auth._AUTH_MODE
AUTH_PASSWORD_VALIDATORS = auth.AUTH_PASSWORD_VALIDATORS
AUTH_USER_MODEL = auth.AUTH_USER_MODEL
AUTHENTICATION_BACKENDS = auth.AUTHENTICATION_BACKENDS
REST_FRAMEWORK = auth.REST_FRAMEWORK
if auth._AUTH_MODE == 'oauth2':
    OAUTH2_PROVIDER = {
        # this is the list of available scopes
        'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
    }

# For emails
EMAIL_BACKEND = std_email.EMAIL_BACKEND
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'authentication/templates'),
)

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
