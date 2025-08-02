from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import os
# Create your models here.

class ImageConversion(models.Model):
    format_choice = [
        ("PNG", "PNG"),
        ("JPEG", "JPEG"),
        ("WEBP", "WEBP"),
        ("GIF", "GIF"),
    ]

    original_image = models.ImageField(upload_to="originals/")
    converted_images = models.ImageField(upload_to="converted/", blank=True, null=True)

    format_form = models.CharField(max_length=10)
    format_to = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_image.name} -> {self.format_to}"

    def convert_image(self):
        # Конвертирует изображения в выбранный формат
        img = Image.open(self.original_image)

        # конвертация в RGB
        if img.mode in ("RGBA", "LA") and self.format_to in ("JPEG", "JPG"):
            img.convert("RGB")

        buffer = BytesIO()

        if self.format_to == "JPEG":
            img.save(buffer, format="JPEG", quality=85, optimize=True)
        elif self.format_to == "PNG":
            img.save(buffer, format="PNG", optimize=True)
        elif self.format_to == "WEBP":
            img.save(buffer, format="WEBP", quality=85)
        elif self.format_to == "GIF":
            img.save(buffer, format="GIF", optimize=True)

        original_name = os.path.splitext(os.path.basename(self.original_image.name))[0]
        new_filename = f"{original_name}_converted.{self.format_to.lower()}"

        # saving image
        self.converted_images.save(
            new_filename,
            ContentFile(buffer.getvalue()),
            save=False
        )
        self.save()


