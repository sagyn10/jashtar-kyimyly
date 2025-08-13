from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    ForgotPasswordView,
    ConfirmResetPasswordView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', ConfirmResetPasswordView.as_view(), name='reset-password'),
]