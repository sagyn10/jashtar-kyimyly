from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from .models import UserProfile, ProjectApplicationLink
from .tokens import custom_token_generator
from django.conf import settings
from django.core.mail import send_mail

class RegisterSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True, label="Подтверждение пароля")

    class Meta:
        model = UserProfile
        fields = ['name', 'second_name', 'surname', 'email', 'password', 'password_confirmation']
        extra_kwargs = {
            'password': {'write_only': True, 'label': 'Пароль'},
        }

    def validate_full_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('ФИО должно содержать минимум 3 символа.')
        for ch in value:
            if not (ch == ' ' or ('А' <= ch <= 'я') or ch in 'ёЁ'):
                raise serializers.ValidationError('ФИО должно содержать только русские буквы.')
        return value

    def validate_email(self, value):
        if not (value.endswith('@gmail.com') or value.endswith('@mail.ru')):
            raise serializers.ValidationError(
                'Email должен быть в формате example@gmail.com или example@mail.ru.'
            )
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Пароль должен содержать минимум 8 символов.')
        if not any(ch.isdigit() for ch in value):
            raise serializers.ValidationError('Пароль должен содержать хотя бы одну цифру.')
        if not any(ch.isupper() for ch in value):
            raise serializers.ValidationError('Пароль должен содержать хотя бы одну заглавную букву.')
        return value

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({'password_confirmation': 'Пароли не совпадают.'})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        password = validated_data.pop('password')
        user = UserProfile(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Электронная почта", required=True)
    password = serializers.CharField(write_only=True, label="Пароль", required=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            user = UserProfile.objects.get(email=email)
        except UserProfile.DoesNotExist:
            raise serializers.ValidationError("Неверный логин или пароль.")

        if not check_password(password, user.password):
            raise serializers.ValidationError("Неверный логин или пароль.")

        if not user.is_active:
            raise serializers.ValidationError("Пользователь деактивирован.")

        data['user'] = user
        return data


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Электронная почта")

    def validate_email(self, value):
        try:
            self.user = UserProfile.objects.get(email=value)
        except UserProfile.DoesNotExist:
            raise serializers.ValidationError("Пользователь с таким email не найден.")
        return value

    def save(self):
        token = custom_token_generator.make_token(self.user)
        reset_link = f"{settings.FRONTEND_URL}/reset-password/{token}?email={self.user.email}"
        try:
            send_mail(
                subject="Восстановление пароля",
                message=f"Для сброса пароля перейдите по ссылке: {reset_link}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[self.user.email]
            )
        except Exception as e:
            raise serializers.ValidationError(f"Ошибка отправки email: {str(e)}")
        return reset_link


class ConfirmResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True, label="Новый пароль")
    new_password_confirmation = serializers.CharField(write_only=True, label="Подтверждение нового пароля")

    def validate_email(self, value):
        try:
            self.user = UserProfile.objects.get(email=value)
        except UserProfile.DoesNotExist:
            raise serializers.ValidationError("Пользователь с таким email не найден.")
        return value

    def validate(self, data):
        if data['new_password'] != data['new_password_confirmation']:
            raise serializers.ValidationError({"new_password_confirmation": "Пароли не совпадают."})

        if not custom_token_generator.check_token(self.user, data['token']):
            raise serializers.ValidationError({"token": "Неверный или просроченный токен."})

        return data

    def save(self):
        self.user.set_password(self.validated_data['new_password'])
        self.user.save()
        return self.user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email']
        extra_kwargs = {
            'email': {'read_only': True}
        }

    def validate_full_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('ФИО должно содержать минимум 3 символа.')
        for ch in value:
            if not (ch == ' ' or ('А' <= ch <= 'я') or ch in 'ёЁ'):
                raise serializers.ValidationError('ФИО должно содержать только русские буквы.')
        return value


class ProjectApplicationLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectApplicationLink
        fields = ['google_form_url']