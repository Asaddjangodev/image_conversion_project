from django import forms
from .models import ImageConversion


class ImageUploadForm(forms.ModelForm):
    class Meta:
        models = ImageConversion
        fields = ['original_name', 'format_to']
        widgets = {
            'format_to': forms.Select(attrs={'class': 'form-control'}),
            'original_image': forms.FileInput(attrs={'class': 'form-control'}),
        }