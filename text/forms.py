from django import forms
from .models import Text


class AddTextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ("text",)
        