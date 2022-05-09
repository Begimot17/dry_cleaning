from django.db import models


class Service(models.Model):
    name = models.TextField(max_length=50, blank=True)
    time = models.DateTimeField(blank=True)
    ownership = models.TextField(null=True)
    preparations = models.TextField(null=True)
    total = models.IntegerField(blank=True)


class Order(models.Model):
    status = models.TextField(max_length=50, blank=True)
    quantity = models.IntegerField(blank=True)
    date_of_receipt = models.DateTimeField(null=True)
    date_of_issue = models.DateTimeField(null=True)
    date_of_process = models.DateTimeField(null=True)
    total = models.IntegerField(blank=True)
    services = models.ManyToManyField(Service)


class Client(models.Model):
    first_name = models.TextField(max_length=50, blank=True)
    middle_name = models.TextField(max_length=50, blank=True)
    last_name = models.TextField(max_length=50, blank=True)
    phone = models.TextField(max_length=50, blank=True)
    orders = models.ManyToManyField(Order)
