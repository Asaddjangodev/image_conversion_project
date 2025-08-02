from django.db import models

# Create your models here.

class ImageConversion(models.Model):
    original_image = models.ImageField(upload_to="originals/")
    converted_images = models.ImageField(upload_to="converted/", blank=True, null=True)

    format_form = models.CharField(max_length=10)
    format_to = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_image.name} -> {self.format_to}"
