from django import forms
from .models import Image ,Video


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'imageFile']


class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile"]
