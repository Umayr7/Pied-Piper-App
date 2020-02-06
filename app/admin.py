from django.contrib import admin
from app.models import ImageCompress, TextCompress, ImageDecompress, TextDecompress

admin.site.register(ImageCompress)
admin.site.register(TextCompress)
admin.site.register(TextDecompress)
admin.site.register(ImageDecompress)
