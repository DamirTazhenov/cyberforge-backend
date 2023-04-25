from rest_framework import generics, mixins
from .models import Modification
from .serializers import *


class ModificationList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Modification.objects.all()
    serializer_class = ModificationsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ModificationDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = Modification.objects.all()
    serializer_class = ModificationsSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CoolingList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Cooling.objects.all()
    serializer_class = CoolingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CoolingDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Cooling.objects.all()
    serializer_class = CoolingSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class HousingList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class HousingDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PowerSupplyUnitList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = PowerSupplyUnit.objects.all()
    serializer_class = PowerSupplyUnitSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PowerSupplyUnitDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = PowerSupplyUnit.objects.all()
    serializer_class = PowerSupplyUnitSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class RAMList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RAMDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GraphicsCardList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = GraphicsCard.objects.all()
    serializer_class = GraphicCardSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GraphicsCardDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = GraphicsCard.objects.all()
    serializer_class = GraphicCardSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class MotherboardList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MotherboardDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProcessorList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProcessorDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer
    lookup_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)