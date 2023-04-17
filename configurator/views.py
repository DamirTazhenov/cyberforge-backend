from rest_framework import generics
from .models import Modification
from .serializers import ConfiguratorSerializer


class ModificationAPIView(generics.ListAPIView):
    queryset = Modification.objects.all()
    serializer_class = ConfiguratorSerializer

