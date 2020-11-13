from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    class meta:
        model = Image
        fields = '__all__'
