from django.urls import path, include
from account.views import verify_reset_code, RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("password_reset/verify_code/", verify_reset_code, name="verify_reset_code"),
    path("password_reset/", include("django_rest_passwordreset.urls", namespace="password_reset")),
]
