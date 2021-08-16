from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class CargoCreateRequestSerializer(serializers.Serializer):
    delivery_type: str = serializers.CharField(help_text="Тип отправления: ['docs', 'parcel']")
    cargo_comment: str = serializers.CharField(default="Груз из ИМ", help_text="Комментарий")
    cargo_type_id: int = serializers.HiddenField(default=32, help_text="Тип груза")
    height: int = serializers.IntegerField(default=10, help_text="Высота в см", min_value=1, max_value=10000)
    length: int = serializers.IntegerField(default=5, help_text="Длина в см", min_value=1, max_value=10000)
    width: int = serializers.IntegerField(default=10, help_text="Ширина в см", min_value=1, max_value=10000)
    quantity: int = serializers.IntegerField(default=1, help_text="Количество мест", min_value=1, max_value=100)
    weight: float = serializers.FloatField(default=0.2, help_text="Вес груза (в кг)", min_value=0.001, max_value=2000)

    def validate(self, attrs):
        if attrs.get("delivery_type") not in ["docs", "parcel"]:
            raise serializers.ValidationError(_('This value should be "docs" or "parcel".'))
        if attrs.get("cargo_type_id") not in [32, 7]:
            raise serializers.ValidationError(_('This value should be equal 32.'))

        return attrs


class CargoCreateResponseSerializer(serializers.Serializer):
    id: int = serializers.IntegerField(help_text="ID груза")
