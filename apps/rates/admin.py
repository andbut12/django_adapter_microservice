from django.contrib import admin

from apps.rates.models import RateRequest


@admin.register(RateRequest)
class RateRequestAdmin(admin.ModelAdmin):
    list_display = ("sender_contact_id", "receiver_contact_id", "cargoes")
