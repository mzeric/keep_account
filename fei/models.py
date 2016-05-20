from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Ren(models.Model):
    name = models.CharField(max_length=50)
    balance = models.FloatField()
    
    def __unicode__(self):
        return self.name

class ChiFan(models.Model):
    addr = models.CharField(max_length=50)
    date = models.DateTimeField()
    ren = models.ManyToManyField(Ren)
    comment = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.addr+" ",self.date

class Charge(models.Model):
    ren = models.ForeignKey(Ren, verbose_name = "who charge")
    money = models.FloatField()

