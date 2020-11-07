from django.urls import path
from authentication.token_auth.views import Login, Logout

urlpatterns = [
    path('login/', Login.as_view(), name='api_token_auth_login'),
    path('logout/', Logout.as_view(), name='api_token_auth_logout'),
]
