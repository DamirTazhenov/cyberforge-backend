from django.urls import path
from .views import ModificationAPIView

app_name = 'configurator'
urlpatterns = [
    path('', ModificationAPIView.as_view(), name='modifications')
]

