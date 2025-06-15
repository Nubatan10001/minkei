from django import forms
from .models import Prof

class ProfForm(forms.ModelForm):
    class Meta:
        model = Prof
        fields = ['name', 'biography', 'specialty', 'profile_image', 'message']