from django.urls import path, include
from account.views import verify_reset_code, RegisterView, LoginView
from account.views import RegisterView, LoginView, verify_email, password_reset_confirm, UserCabinetView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("password_reset/verify_code/", verify_reset_code, name="verify_reset_code"),
    path("password_reset/", include("django_rest_passwordreset.urls", namespace="password_reset")),
    path("verify-email/", verify_email, name="verify_email"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # сброс пароля
    path("password_reset/", include("django_rest_passwordreset.urls", namespace="password_reset")),
    path("password_reset/confirm/", password_reset_confirm, name="password_reset_confirm"),

    path("cabinet/", UserCabinetView.as_view(), name="user_cabinet"),

]
