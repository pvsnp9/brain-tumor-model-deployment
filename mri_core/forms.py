from django import forms
from .models import MriImage


class ImageFileUploadForm(forms.ModelForm):
    class Meta:
        model = MriImage
        fields = ('mri_image', ) 