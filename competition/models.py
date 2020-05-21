from django.db import models
import datetime
from django.contrib.auth.models import User

class Competition(models.Model):

    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    match1 = models.CharField(max_length=254, default='bsdfsd')
    sascore1 = models.IntegerField()
    lionsscore1 = models.IntegerField()
    submit_date = models.DateField(default=datetime.date.today)

    

    def __str__(self):
        return f'{self.id}-{self.customer.username}'