from django.db import models
from django.conf import settings
from treatments.models import Massage

# Create your models here.


TIME_CHOICES = [
    ('9AM-10AM', '9AM-10AM'), ('10AM-11AM', '10AM-11AM'),
    ('11AM-12PM', '11AM-12PM'), ('1PM-2PM', '1PM-2PM'),
    ('2PM-3PM', '2PM-3PM'), ('3PM-4PM', '3PM-4PM'),
    ('4PM-5PM', '4PM-5PM'),
]


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    massage = models.ForeignKey(Massage, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=10, choices=TIME_CHOICES)

    def __str__(self):
        return f"{self.user.username}'s booking for {self.massage.name} on {self.date} at {self.time_slot}"
