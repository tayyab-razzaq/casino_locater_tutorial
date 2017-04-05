from rest_framework import serializers

from casino_finder.models import Casino


class CasinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casino
        fields = ('id', 'name', 'address')
