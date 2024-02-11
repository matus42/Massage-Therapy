from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Massage(models.Model):
    name = models.CharField(max_length=100)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.name
