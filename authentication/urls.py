from django.urls import path
from authentication.views import Login, Logout
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', Login.as_view(), name='api_token_auth_login'),
    path('logout/', Logout.as_view(), name='api_token_auth_logout'),
]
