from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema

from .serializers import RegisterSerializer, LoginSerializer, VerifyResetCodeSerializer


@extend_schema(
    tags=['account'],
    summary="Регистрация нового пользователя",
    description="Создаёт нового пользователя по email и паролю"
)
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


@extend_schema(
    tags=['account'],
    summary="Авторизация пользователя",
    description="Возвращает пару JWT токенов (refresh + access) и данные пользователя"
)
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "email": user.email,
                "full_name": user.full_name,
            }
        }, status=status.HTTP_200_OK)


@extend_schema(
    tags=['account'],
    summary="Проверка кода сброса пароля",
    description="Проверяет введённый 4-значный код и устанавливает новый пароль"
)
@api_view(['POST'])
def verify_reset_code(request):
    serializer = VerifyResetCodeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Пароль успешно сброшен.'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
