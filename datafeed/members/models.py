from django.db import models
import datetime

class Member(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    amt_pur = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name+ ', '+self.place+', '+str(self.phone)+', '+str(self.amt_pur)+', '+str(self.date)
