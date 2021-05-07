from django.contrib import admin
from django.urls import path, re_path
from django.urls import include, path
from django.conf.urls.static import static
from drf_api import settings
from rest_auth.registration.views import VerifyEmailView, RegisterView
from rest_framework.authtoken.views import obtain_auth_token
from allauth.account.views import ConfirmEmailView
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testView/', getCourses.as_view(), name="test"),
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
    path('get-courses', getCourses.as_view(), name='test'),
    path('get-instructor', getInstructor.as_view(), name='test-Instructor'),
    path('get-instructor-rev', getInstructorReviews.as_view(), name='test-Instructor-Rev'),
    path('get-course-rev', getCourseReviews.as_view(), name='test-Course-Rev'),
    path('get-course-rev-votes', getCourseReviewVotes.as_view(), name='test-Course-Rev-votes'),
    path('get-course-rev-tags', getCourseReviewTags.as_view(), name='test-Course-Rev-tags'),
    path('get-instructor-rev-votes', getInstructorReviewVotes.as_view(), name='test-Course-Rev-votes'),
    path('get-instructor-rev-tags', getInstructorReviewTags.as_view(), name='test-Course-Rev-tags'),
    path('api/token', obtain_auth_token, name = 'obtain_token' )
]

