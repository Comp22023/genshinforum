from django import forms
from .models import *


class ThemesForm(forms.ModelForm):
    class Meta:
        model = Themes
        fields = '__all__'
