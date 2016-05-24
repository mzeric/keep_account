from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

# Create your models here.
class Ren(models.Model):
    name = models.CharField(max_length=50)
    balance = models.FloatField(editable=True)
    
    def __unicode__(self):
        return self.name


class ChiFan(models.Model):
    addr = models.CharField(max_length=50)
    date = models.DateTimeField(_("Date"), default = timezone.now)
    ren = models.ManyToManyField(Ren)
    comment = models.CharField(max_length=1024)
    cost_sharing = models.FloatField(default=0.0)
    total = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.addr

class ChiFan_Sep(models.Model):
    ren = models.ForeignKey(Ren)
    cost = models.FloatField()
    chifan = models.ForeignKey(ChiFan)
    comment = models.CharField(max_length=1024)

class Charge(models.Model):
    ren = models.ForeignKey(Ren)
    money = models.FloatField(verbose_name=_("Charge"))
    date = models.DateTimeField(_("Date"), default = timezone.now)

    def __unicode_(self):
        return self.ren.name
