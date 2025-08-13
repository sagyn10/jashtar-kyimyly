from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    ForgotPasswordSerializer,
    ConfirmResetPasswordSerializer
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter

@extend_schema(
    tags=["account"],
    request=RegisterSerializer,
    responses={
        201: OpenApiResponse(description="Успешная регистрация"),
        400: OpenApiResponse(description="Ошибка валидации данных")
    }
)
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'user': {
                    'id': user.id,
                    'full_name': user.full_name,
                    'email': user.email
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=["account"],
    request=LoginSerializer,
    responses={
        200: OpenApiResponse(description="Успешный вход"),
        400: OpenApiResponse(description="Ошибка валидации данных")
    }
)
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({
                'user': {
                    'id': user.id,
                    'full_name': user.full_name,
                    'email': user.email
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=["account"],
    request=ForgotPasswordSerializer,
    responses={
        200: OpenApiResponse(description="Ссылка для сброса пароля сгенерирована"),
        400: OpenApiResponse(description="Ошибка валидации данных")
    }
)
class ForgotPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            reset_link = serializer.save()
            return Response({
                'message': 'Ссылка для сброса пароля сгенерирована',
                'reset_link': reset_link
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=["account"],
    request=ConfirmResetPasswordSerializer,
    responses={
        200: OpenApiResponse(description="Пароль успешно изменен"),
        400: OpenApiResponse(description="Ошибка валидации данных")
    }
)
class ConfirmResetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ConfirmResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'Пароль успешно изменен'
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)