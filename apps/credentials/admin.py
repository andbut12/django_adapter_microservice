from django.contrib import admin

from apps.credentials.forms import CredentialsForm
from apps.credentials.models import Credentials


@admin.register(Credentials)
class CredentialsAdmin(admin.ModelAdmin):
    form = CredentialsForm
    list_filter = ("is_blocked",)
    list_display = ("eshop", "token", "created_at")
    search_fields = ("eshop", "token__exact")
    readonly_fields = ("token",)
