from authentication import urls as auth_urls
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from user import urls as user_urls

app_urls = [
    path('user/', include(user_urls)),
    path('auth/', include(auth_urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Base App API Docs', public=False)),
    path('api/v1/', include(app_urls)),
]
