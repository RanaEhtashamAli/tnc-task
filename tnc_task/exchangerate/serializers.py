from rest_framework import serializers
from .models import ExchangeRate


class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ['from_currency_code', 'from_currency_name', 'to_currency_code', 'to_currency_name',
                  'exchange_rate', 'last_refreshed', 'time_zone', 'bid_price', 'ask_price']

    def create(self, validated_data):
        return ExchangeRate.objects.create(**validated_data)


class APIKeySerializer(serializers.Serializer):
    key_name = serializers.CharField(max_length=50)
