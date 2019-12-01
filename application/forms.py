from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model=Application
        fields=['title', 'body1', 'body2', 'body3', 'body4', 'body5', 'body6']