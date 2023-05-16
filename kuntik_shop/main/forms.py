from django import forms

from .models import UserPost
from django.forms import ModelForm, TextInput, Textarea


class UserPostForm(ModelForm):
    class Meta:
        model = UserPost
        fields = ['color', 'material', 'size', 'options']
        widgets ={
            "color": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цвет'
            }),
            "material": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите желаемый материал изделия'
            }),
            "size": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите размер'
            }),
            "options": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дополнительные опции'
            }),
        }