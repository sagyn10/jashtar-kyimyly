from django.urls import path, include
from account.views import verify_reset_code

urlpatterns = [
    path('password_reset/verify_code/', verify_reset_code, name='verify_reset_code'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
