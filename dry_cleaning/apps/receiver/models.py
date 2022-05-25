from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Service(models.Model):
    name = models.TextField(max_length=50, blank=True)
    time = models.DateTimeField(blank=True)
    ownership = models.TextField(null=True)
    preparations = models.TextField(null=True)
    total = models.IntegerField(blank=True)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.TextField(max_length=50, blank=True)
    quantity = models.IntegerField(blank=True)
    date_of_receipt = models.DateTimeField(null=True)
    date_of_issue = models.DateTimeField(null=True)
    date_of_process = models.DateTimeField(null=True)
    total = models.IntegerField(blank=True)
    services = models.ManyToManyField(Service)



