from base_app.settings import _AUTH_MODE
from authentication.token_auth import urls as token_auth_urls
from django.urls import path, re_path, include

# Determine authentication urls to use
auth_path = []
if _AUTH_MODE == 'token_auth':
    auth_path = path('', include(token_auth_urls))
elif _AUTH_MODE == 'oauth2':
    pass


urlpatterns = [
    auth_path,
    re_path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
