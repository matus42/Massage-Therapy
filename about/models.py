from django.db import models
from cloudinary.models import CloudinaryField


class AboutPage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.name
