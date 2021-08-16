from django import forms
from django.forms import PasswordInput

from apps.credentials.models import Credentials


class CredentialsForm(forms.ModelForm):
    class Meta:
        model = Credentials
        exclude = []
        widgets = {
            'password': PasswordInput(),
        }
