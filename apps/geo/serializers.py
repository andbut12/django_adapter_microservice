from rest_framework import serializers


class SearchGeoRequestSerializer(serializers.Serializer):
    term: str = serializers.CharField(max_length=32, default="Москва", min_length=2)
    iso: str = serializers.CharField(max_length=8, default="ru", min_length=1)
    limit: int = serializers.IntegerField(max_value=50, default=50, min_value=1)


class SearchGeoResponseSerializer(serializers.Serializer):
    id: int = serializers.IntegerField()
    locality: str = serializers.CharField()
    zip: int = serializers.IntegerField()
