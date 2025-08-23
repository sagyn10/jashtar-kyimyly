from django_rest_passwordreset.models import ResetPasswordToken
from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from .models import UserProfile


class RegisterSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ['name', 'second_name', 'surname', 'full_name', 'email', 'password', 'password_confirmation']
        extra_kwargs = {
            'password': {'write_only': True}
        }

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
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

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

class VerifyResetCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()  # Email пользователя
    reset_code = serializers.IntegerField()  # 4-значный код
    new_password = serializers.CharField(write_only=True)  # Новый пароль

    def validate(self, data):
        email = data.get('email')
        reset_code = data.get('reset_code')

        # Проверяем, существует ли указанный код для email
        try:
            token = ResetPasswordToken.objects.get(user__email=email, key=reset_code)
        except ResetPasswordToken.DoesNotExist:
            raise serializers.ValidationError("Неверный код сброса или email.")

        data['user'] = token.user
        return data

    def save(self):
        user = self.validated_data['user']
        new_password = self.validated_data['new_password']

        # Устанавливаем новый пароль
        user.set_password(new_password)
        user.save()
