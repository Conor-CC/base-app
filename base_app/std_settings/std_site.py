from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-d_ip+_=z%7lsj+od=9jrs!pa0dva2&$so0p%&ik2kqv#jc&#0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ROOT_URLCONF = 'base_app.urls'
WSGI_APPLICATION = 'base_app.wsgi.application'

ALLOWED_HOSTS = []


_SITE_APPS = [
    # Site Apps
    'user',
]

_TEST_APPS = [
    # Test Suite
    'tests',
    'tests.test_models',
    'tests.test_views',
    'tests.test_endpoints',
]

SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
