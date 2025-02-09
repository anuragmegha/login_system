from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
