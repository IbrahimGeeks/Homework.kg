from django import forms
from .models import Tourist, Horse

class TouristForm(forms.ModelForm):
    class Meta:
        model = Tourist
        fields = ['name', 'horse']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'horse': forms.Select(attrs={'class': 'form-control'}),
        }