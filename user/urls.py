from dj_rest_auth.registration.views import VerifyEmailView
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views

urlpatterns = [
    path('list-user/', views.UserView_List.as_view(), name=''),
    path('list-user-type-one/', views.UserTypeOneView_List.as_view(), name=''),
    path('create-user-type-one/', views.UserTypeOneView_Create.as_view(), name=''),
    path('retrieve-update-user-type-one/<int:pk>/', views.UserTypeOneView_RetrieveUpdate.as_view(), name=''),
    path('destroy-user-type-one/<int:pk>/', views.UserTypeOneView_Destroy.as_view(), name=''),
    re_path(r'^account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
