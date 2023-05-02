from rest_framework_jwt.settings import api_settings
from rest_framework import serializers, status
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_simplejwt.tokens import RefreshToken

from configurator.serializers import ModificationSerializer, ModificationGetSerializer
from .models import User


class CustomObtainJSONWebToken(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainJSONWebToken, self).post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            token = response.data['token']
            jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
            user_id = jwt_decode_handler(token)['user_id']
            user = User.objects.get(id=user_id)
            user_serializer = UserSerializer(user)
            response.data['user'] = user_serializer.data
        return response


class UserSerializer(serializers.ModelSerializer):
    modifications = ModificationSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'username', 'password', 'modifications')
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ['modifications']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password is not None:
            user.set_password(password)
            user.save()

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }

