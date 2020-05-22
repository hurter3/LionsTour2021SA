from django.db import models
import datetime
from django.contrib.auth.models import User

class Competition(models.Model):

    customer = models.ForeignKey(User, on_delete=models.PROTECT)
  
    sascore1 = models.PositiveSmallIntegerField(default=0)
    lionsscore1 = models.PositiveSmallIntegerField(default=0)
    sascore2 = models.PositiveSmallIntegerField(default=0)
    lionsscore2 = models.PositiveSmallIntegerField(default=0)
    sascore3 = models.PositiveSmallIntegerField(default=0)
    lionsscore3 = models.PositiveSmallIntegerField(default=0)
    sascore4 = models.PositiveSmallIntegerField(default=0)
    lionsscore4 = models.PositiveSmallIntegerField(default=0)
    sascore5 = models.PositiveSmallIntegerField(default=0)
    lionsscore5 = models.PositiveSmallIntegerField(default=0)
    sascore6 = models.PositiveSmallIntegerField(default=0)
    lionsscore6 = models.PositiveSmallIntegerField(default=0)
    sascore7 = models.PositiveSmallIntegerField(default=0)
    lionsscore7 = models.PositiveSmallIntegerField(default=0)
    sascore8 = models.PositiveSmallIntegerField(default=0)
    lionsscore8 = models.PositiveSmallIntegerField(default=0)
    points_accrued = models.PositiveSmallIntegerField(default=0)
    
    submit_date = models.DateField(default=datetime.date.today)    

    def __str__(self):
        return f'{self.id}-{self.customer.username}'