from django import forms
from .models import ImageCompress, TextCompress, TextDecompress, ImageDecompress


class GetImageForm(forms.ModelForm):
    class Meta:
        model = ImageCompress
        fields = [
            'image'
        ]


class GetTextForm(forms.ModelForm):
    class Meta:
        model = TextCompress
        fields = [
            'text'
        ]


class GetDecompressTextForm(forms.ModelForm):
    class Meta:
        model = TextDecompress
        fields = [
            'decompress_text'
        ]


class GetDecompressImageForm(forms.ModelForm):
    class Meta:
        model = ImageDecompress
        fields = [
            'decompress_image'
        ]