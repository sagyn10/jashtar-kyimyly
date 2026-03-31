from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
from django.db.models import Prefetch
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.http import HttpResponse

from content.models import Projects, EducationMaterial
from .serializers import RegisterSerializer, LoginSerializer, PasswordResetConfirmSerializer, UserCabinetSerializer, VerifyEmailSerializer
from .models import UserProfile, UserCabinet


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        token = default_token_generator.make_token(user)
        
        # Меняем хардкод ngrok на  домен Railway!
        domain = "jashtar-kyimyly.up.railway.app" # или ссылка на фронтенд
        confirm_link = f"https://{domain}/api/account/verify-email?uid={user.pk}&token={token}"

        send_mail(
            "Подтверждение email",
            f"Для подтверждения перейдите по ссылке: {confirm_link}",
            "noreply@jashtar.kg", 
            [user.email],
            fail_silently=False,
        )


@extend_schema(request=VerifyEmailSerializer, responses={200: dict, 400: dict})
@api_view(['POST'])
def verify_email(request):
    uid = request.data.get("uid")
    token = request.data.get("token")
    try:
        user = UserProfile.objects.get(pk=uid)
    except UserProfile.DoesNotExist:
        return Response({"error": "Пользователь не найден"}, status=400)

    from django.contrib.auth.tokens import default_token_generator
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return Response({"message": "Email подтверждён"}, status=200)
    return Response({"error": "Неверный токен"}, status=400)


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


@api_view(['POST'])
def password_reset_confirm(request):
    serializer = PasswordResetConfirmSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Пароль успешно сброшен.'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCabinetView(generics.RetrieveUpdateAPIView):
    serializer_class = UserCabinetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self): # type: ignore
        return (
            UserCabinet.objects.select_related(
                "user"
            ).prefetch_related(
                Prefetch("projects", queryset=Projects.objects.prefetch_related('images')),
                "education_materials"
            ).get(user=self.request.user)
        )

def create_magic_admin(request):
    User = get_user_model()
    email = "super@railway.com"
    password = "SuperPassword123"

    if not User.objects.filter(email=email).exists():
        user = User.objects.create_superuser(email=email, password=password, full_name="Главный Админ")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return HttpResponse(f"УСПЕХ! Создан админ.<br>Логин: {email}<br>Пароль: {password}")
    
    return HttpResponse("Админ уже был создан ранее! Можешь логиниться.")