from django.db import models
from django.contrib.auth.models import User


class Chemicals(models.Model):
    name = models.TextField(max_length=50, blank=True)
    quantity = models.IntegerField(blank=True)
    type = models.TextField()
    type_by_use = models.TextField()
    instruction = models.TextField()


class Shifts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.TextField(max_length=50, blank=True)
    spent_changes = models.IntegerField(blank=True)
