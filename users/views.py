from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken

from users.serializers import UserSerializer

User = get_user_model()


class CustomObtainJSONWebToken(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainJSONWebToken, self).post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            token = response.data['token']
            jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
            user_id = jwt_decode_handler(token)['user_id']
            user = User.objects.get(id=user_id)
            user_serializer = UserSerializer(user, context={'request': request})
            response.data['user'] = user_serializer.data
        return response


class RegisterPageAPIView(ObtainJSONWebToken):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.create(serializer.validated_data).get('username')

        auth_user = authenticate(username=username, password=request.data['password'])
        if auth_user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        payload = jwt_payload_handler(auth_user)
        token = jwt_encode_handler(payload)

        response = Response({'token': token, 'user': serializer.data}, status=status.HTTP_201_CREATED)

        return response


class UserAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user, context={'request': request})

            return Response(serializer.data)
        else:
            raise AuthenticationFailed('Unauthenticated!')


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        response = Response()
        response['Authorization'] = ''
        response.data = {
            "message": "Successfully logged out."
        }
        return response
