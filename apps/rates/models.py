from django.db import models


class RateRequest(models.Model):
    sender_contact_id = models.IntegerField(null=True, blank=True)
    receiver_contact_id = models.IntegerField(null=True, blank=True)
    cargoes = models.CharField(null=True, blank=True, max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Запрос на создание расчета"
        verbose_name_plural = "Запросы на создание расчета"
