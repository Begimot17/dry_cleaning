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

class Possession(models.Model):
    name = models.TextField(max_length=50, blank=True)
    type = models.TextField(max_length=50, blank=True)
    service = models.TextField(max_length=50, blank=True)
    chemical = models.TextField(max_length=50, blank=True)
    cost = models.TextField(max_length=50, blank=True)
    hour = models.TextField(max_length=50, blank=True)
    date = models.TextField(max_length=50, blank=True)



