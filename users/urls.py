from django.urls import path

from .views import RegisterPageAPIView, UserAPIView, CustomObtainJSONWebToken

app_name = 'users'

urlpatterns = [
    path('login/', CustomObtainJSONWebToken.as_view(), name='login'),
    path('register/', RegisterPageAPIView.as_view(), name='register'),
    path('user/', UserAPIView.as_view(), name='user_view'),
    # path('logout/', LogoutAPIView.as_view(), name='logout'),
]
