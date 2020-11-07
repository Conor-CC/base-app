_AUTH_MODE = 'token_auth'

_AUTH_APPS = [
    # Third Party Apps
    'rest_framework',
    'rest_framework.authtoken',
    'django_rest_passwordreset',
    'authentication',
]

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'user.UserModel_Base'

AUTHENTICATION_BACKENDS = {
    "django.contrib.auth.backends.ModelBackend",
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'authentication.token_auth.authenticators.TokenAuthentication',
        # 'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ],
    'TOKEN_EXPIRY_TIME_SEC': 43200,  # 12 hours in seconds
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}
