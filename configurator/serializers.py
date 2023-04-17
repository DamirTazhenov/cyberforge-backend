from rest_framework import serializers
from .models import Modification


class ConfiguratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modification
        fields = ('housing', 'motherboard', 'power_supply', 'processor', 'graphic_card', 'ram', 'memory', 'cooling', 'accessories')