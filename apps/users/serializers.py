import re

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class ContactCreateRequestSerializer(serializers.Serializer):
    locality_id: int = serializers.IntegerField(required=True, help_text="ID геообъекта (из справочника городов)")
    zip: int = serializers.IntegerField(required=True, help_text="Почтовый индекс (из справочника городов)")
    street: str = serializers.CharField(help_text="Улица")
    building: str = serializers.CharField(help_text="Здание")
    door_number: str = serializers.CharField(help_text="Офис/квартира")
    comment: str = serializers.CharField(help_text="Комментарий", required=False)
    company: str = serializers.CharField(help_text="Компания", required=False)
    name: str = serializers.CharField(help_text="ФИО")
    phone: str = serializers.CharField(default="+78001112233", help_text="Телефон")
    iso: str = serializers.CharField(default="ru", help_text="Код страны")

    def validate(self, attrs):
        phone = attrs.get("phone")
        if not (phone and re.search("\+\d{3}\d{3}\d{4}", phone)):
            raise serializers.ValidationError(_('This value should be formatted as "+78001112233".'))
        return attrs


class ContactCreateResponseSerializer(serializers.Serializer):
    id: int = serializers.IntegerField()


class ContactUpdateRequestSerializer(serializers.Serializer):
    locality_id: int = serializers.IntegerField(required=True, help_text="ID геообъекта (из справочника городов)")
    zip: int = serializers.IntegerField(required=True, help_text="Почтовый индекс (из справочника городов)")
    street: str = serializers.CharField(help_text="Улица")
    building: str = serializers.CharField(help_text="Здание")
    door_number: str = serializers.CharField(help_text="Офис/квартира")
    comment: str = serializers.CharField(help_text="Комментарий", required=False)
    company: str = serializers.CharField(help_text="Компания", required=False)
    name: str = serializers.CharField(help_text="ФИО")
    phone: str = serializers.CharField(default="+78001112233", help_text="Телефон")
    iso: str = serializers.CharField(default="ru", help_text="Код страны")

    def validate(self, attrs):
        phone = attrs.get("phone")
        if not (phone and re.search("\+\d{3}\d{3}\d{4}", phone)):
            raise serializers.ValidationError(_('This value should be formatted as "+78001112233".'))
        return attrs


class ContactUpdateResponseSerializer(serializers.Serializer):
    id: int = serializers.IntegerField()
