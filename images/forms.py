from django import forms
from .models import ImageConversion


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageConversion
        fields = ['original_image', 'format_to']
        widgets = {
            'format_to': forms.Select(attrs={'class': 'form-control'}),
            'original_image': forms.FileInput(attrs={'class': 'form-control'}),
        }