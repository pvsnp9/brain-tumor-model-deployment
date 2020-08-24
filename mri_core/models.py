from django.db import models
from django.contrib.auth.models import User

class MriImage(models.Model):
    mri_image = models.ImageField(upload_to="images")