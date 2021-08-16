import typing as tp

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class RateCreateRequestSerializer(serializers.Serializer):
    sender_contact_id: int = serializers.IntegerField(
        required=True, help_text="ID контакта отправителя (можно взять ID геообъекта)", min_value=0
    )
    receiver_contact_id: int = serializers.IntegerField(
        required=True, help_text="ID контакта получателя (можно взять ID геообъекта)", min_value=0
    )
    cargoes: tp.List[int] = serializers.ListField(
        child=serializers.IntegerField(required=True, help_text="ID груза"), required=True, min_length=1
    )


class RateCreateResponseSerializer(serializers.Serializer):
    key: str = serializers.CharField(help_text="KEY расчета")


class RateSerializer(serializers.Serializer):
    id: int = serializers.IntegerField()
    operator: str = serializers.CharField(help_text="Название КС")
    rate: str = serializers.CharField(help_text="Название тарифа КС")
    rate_description: str = serializers.CharField(
        help_text="Доставка почтовых и грузовых отправлений в оптимальные сроки по экономичным тарифам.\n\n"
                  "Максимальный физический вес одного места не более 80 кг. Сумма трех измерений - не более 270 см. "
                  "При превышении указанных габаритов взимается доп.сбор в размере 50% от основного тарифа. "
                  "Отправка хрупкого груза ( в том числе предметов из стекла, пластика) рассчитывается +50% к тарифу.",
        allow_blank=True,
        allow_null=True,
    )
    pickup_day: str = serializers.DateField(
        default="2021-05-04",
        help_text="Дата сбора",
        allow_null=True,
    )
    delivery_day: str = serializers.DateField(
        default="2021-05-13",
        help_text="Дата доставки",
        allow_null=True,
    )
    delivery_time: str = serializers.CharField(
        default="19:00",
        help_text="Время доставки до",
        allow_blank=True,
        allow_null=True,
    )
    price: int = serializers.IntegerField(default=2048, help_text="Стоимость, руб.")
    shipping_type: str = serializers.CharField(help_text="Тип доставки.")


class RateRetrieveRequestSerializer(serializers.Serializer):
    shipping_type_filter: str = serializers.CharField(
        default="d2d",
        help_text="Фильтр по типу отправлений: ['d2d', 'd2w', 'w2d', 'w2w']"
    )

    def validate(self, attrs):
        if attrs.get("shipping_type_filter") not in ["d2d", "d2w", "w2d", "w2w"]:
            raise serializers.ValidationError(_('This value should equal to any of ["d2d", "d2w", "w2d", "w2w"].'))

        return attrs


class RateRetrieveResponseSerializer(serializers.Serializer):
    count: int = serializers.IntegerField(help_text="Кол-во полученных предложений от КС")
    results: tp.List[tp.Any] = serializers.ListField(child=RateSerializer(), help_text="Список результатов расчета ")
