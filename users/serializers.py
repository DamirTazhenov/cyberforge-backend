from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from configurator.serializers import ModificationGetSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    modifications = ModificationGetSerializer(many=True, read_only=True)



    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'username', 'password', 'modifications', 'likes')
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ['modifications']


    def create(self, validated_data):
        request = self.context.get('request')

        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
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
            'last_name': user.last_name
        }

