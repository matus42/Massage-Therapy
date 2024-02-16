from django.db import models
from django.conf import settings
from treatments.models import Massage

# Create your models here.


TIME_CHOICES = [
    ('9am-10am', '9am-10am'), ('10am-11am', '10am-11am'),
    ('11am-12pm', '11am-12pm'), ('1pm-2pm', '1pm-2pm'),
    ('2pm-3pm', '2pm-3pm'), ('3pm-4pm', '3pm-4pm'),
    ('4pm-5pm', '4pm-5pm'),
]


STATUS_CHOICES = [
    ('pending', 'Pending Approval'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
]


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    massage = models.ForeignKey(Massage, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=10, choices=TIME_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='pending')

    def __str__(self):
        return (f"{self.user.username}'s booking for {self.massage.name} "
                f"on {self.date} at {self.time_slot}")
