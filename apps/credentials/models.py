import secrets

from django.db import models


def _generate_token() -> str:
    return secrets.token_hex(nbytes=64)


class Credentials(models.Model):
    eshop = models.CharField(max_length=128)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

    token = models.CharField(max_length=128, default=_generate_token)
    example_token = models.CharField(max_length=128, blank=True, null=True)
    is_blocked = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Магазин: {self.eshop}"

    class Meta:
        verbose_name = "Доступ"
        verbose_name_plural = "Доступы"
