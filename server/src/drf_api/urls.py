from django.contrib import admin
from django.urls import path, re_path
from django.urls import include, path
from rest_auth.registration.views import VerifyEmailView, RegisterView
from allauth.account.views import ConfirmEmailView
from core.views import getCourses

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'dj-rest-auth/registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
    ), 
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path(
        'dj-rest-auth/account-confirm-email/',
        VerifyEmailView.as_view(),
        name='account_email_verification_sent'
    ),
    
    
    # path('rest-auth/', include('rest_auth.urls')),
    path('get-courses', getCourses.as_view(), name='test'),
    # path(
    #     'rest-auth/registration/account-confirm-email/<str:key>/',
    #     ConfirmEmailView.as_view(),
    # ),
    # re_path(
    #     r'rest-auth/registration/account-confirm-email/(?P<key>.+)/',
    #     VerifyEmailView.as_view(),
    #     name='account_email_verification_sent'
    # ),
    # re_path(r'rest-auth/registration/account-confirm-email/(?P<key>.+)/', VerifyEmailView.as_view(), name='account_confirm_email'),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
