from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.TextField(max_length=500, blank=True)
    phone= models.TextField(max_length=500, blank=True)
    total= models.IntegerField(null=True)
