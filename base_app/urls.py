from django.contrib import admin
from django.urls import path, include
from user import urls as user_urls
from authentication import urls as auth_urls

app_urls = [
    path('user/', include(user_urls)),
    path('auth/', include(auth_urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(app_urls)),
]
