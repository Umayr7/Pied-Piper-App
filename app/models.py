from django.db import models
from PIL import Image


class ImageCompress(models.Model):
    image = models.ImageField(default=None, upload_to='photos')

    def __str__(self):
        return f'photo to compress'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)


class TextCompress(models.Model):
    text = models.FileField(default=None, upload_to='text', max_length=254)

    def __str__(self):
        return f'text to compress'


class TextDecompress(models.Model):
    decompress_text = models.FileField(default=None, upload_to='text', max_length=254)

    def __str__(self):
        return f'text to decompress'


class ImageDecompress(models.Model):
    decompress_image = models.FileField(default=None, upload_to='text', max_length=254)

    def __str__(self):
        return f'photo to decompress'