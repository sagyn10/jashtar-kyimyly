import re
from django_rest_passwordreset.models import ResetPasswordToken
from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from .models import UserProfile, UserCabinet


class RegisterSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ['name', 'second_name', 'surname', 'full_name', 'email', 'password', 'password_confirmation']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_full_name(self, value):
        if not re.fullmatch(r'[А-Яа-яЁё\s]{3,}', value):
            raise serializers.ValidationError("ФИО должно быть минимум 3 символа и только кириллица.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Пароль должен содержать минимум 8 символов.")
        if not re.search(r'\d', value):
            raise serializers.ValidationError("Пароль должен содержать хотя бы одну цифру.")
        if not re.search(r'[A-ZА-Я]', value):
            raise serializers.ValidationError("Пароль должен содержать хотя бы одну заглавную букву.")
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
        user.is_active = False
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
            raise serializers.ValidationError("Подтвердите email для входа.")

        data['user'] = user
        return data


# class VerifyResetCodeSerializer(serializers.Serializer):

class PasswordResetConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    reset_code = serializers.IntegerField()
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        reset_code = data.get('reset_code')

        try:
            token = ResetPasswordToken.objects.get(user__email=email, key=str(reset_code))
        except ResetPasswordToken.DoesNotExist:
            raise serializers.ValidationError("Неверный код сброса или email.")

        data['user'] = token.user
        return data

    def save(self):
        user = self.validated_data['user']
        new_password = self.validated_data['new_password']
        user.set_password(new_password)
        user.save()


class UserCabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCabinet
        fields = ['telegram_channel', 'google_form_link', 'education_materials']
