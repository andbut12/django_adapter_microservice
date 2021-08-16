import datetime

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class ShipmentCreateRequestSerializer(serializers.Serializer):
    sender_contact_id: int = serializers.IntegerField(required=True, help_text="ID контакта отправителя", min_value=0)
    receiver_contact_id: int = serializers.IntegerField(required=True, help_text="ID контакта получателя", min_value=0)
    rate_result_id: int = serializers.IntegerField(required=True, help_text="ID результата расчета", min_value=0)
    pickup_day: str = serializers.CharField(
        default=datetime.datetime.now().strftime("%d.%m.%Y"),
        help_text="Дата забора (01.01.1997)"
    )

    def validate(self, attrs):
        pickup_datetime = datetime.datetime.strptime(attrs.get("pickup_day"), "%d.%m.%Y")
        if pickup_datetime < datetime.datetime.now():
            raise serializers.ValidationError(
                _(f'Date should be later then "{datetime.datetime.now().strftime("%d.%m.%Y")}".')
            )
        return attrs


class ShipmentCreateResponseSerializer(serializers.Serializer):
    status: str = serializers.CharField(default="success", help_text="Статус (успех/неуспех)")
