from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    amt_pur = models.IntegerField()
    on_or_of = models.CharField(max_length=3)
    date = models.DateField()
