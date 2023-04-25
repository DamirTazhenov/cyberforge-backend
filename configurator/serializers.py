from rest_framework import serializers
from .models import Modification, Cooling, Housing, PowerSupplyUnit, RAM, GraphicsCard, Motherboard, Processor


class ModificationsSerializer(serializers.ModelSerializer):
    is_compatible = serializers.BooleanField(read_only=True)

    class Meta:
        model = Modification
        fields = '__all__'


class CoolingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooling
        fields = '__all__'


class HousingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housing
        fields = '__all__'


class PowerSupplyUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerSupplyUnit
        fields = '__all__'


class RAMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAM
        fields = "__all__"


class GraphicCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraphicsCard
        fields = '__all__'


class MotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motherboard
        fields = '__all__'


class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = '__all__'