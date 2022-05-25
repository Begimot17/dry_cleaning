from django.db import models


class Expenses(models.Model):
    lease = models.IntegerField()
    utilities = models.IntegerField()
    equipment = models.IntegerField()
    salary = models.IntegerField()
    materials = models.IntegerField()
    preparations = models.IntegerField()
    date= models.DateTimeField(null=True)