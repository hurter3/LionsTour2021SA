from django.db import models
import datetime
from django.contrib.auth.models import User

FIRST_POINTS_SELECT = (
    ('NO POINTS SCORED', 'No Points Scored'),
    ('HOME TEAM TRY', 'Home Team Try'),
    ('HOME TEAM PENALTY', 'Home Team Penalty'),
    ('HOME TEAM DROP GOAL', 'Home Team Drop Goal'),
    ('LIONS TEAM TRY', 'Lions Try'),
    ('LIONS PENALTY', 'Lions Penalty'),
    ('LIONS DROP GOAL', 'Lions Drop Goal'),
)


class Competition(models.Model):

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    sascore1 = models.PositiveSmallIntegerField(default=0)
    lionsscore1 = models.PositiveSmallIntegerField(default=0)
    firstpoints1 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
    matchpoints1 = models.PositiveSmallIntegerField(default=0)
    sascore2 = models.PositiveSmallIntegerField(default=0)
    lionsscore2 = models.PositiveSmallIntegerField(default=0)
    firstpoints2 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
    matchpoints2 = models.PositiveSmallIntegerField(default=0)
    sascore3 = models.PositiveSmallIntegerField(default=0)
    lionsscore3 = models.PositiveSmallIntegerField(default=0)
    firstpoints3 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
    matchpoints3 = models.PositiveSmallIntegerField(default=0)
    sascore4 = models.PositiveSmallIntegerField(default=0)
    lionsscore4 = models.PositiveSmallIntegerField(default=0)
    firstpoints4 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
    matchpoints4 = models.PositiveSmallIntegerField(default=0)
    sascore5 = models.PositiveSmallIntegerField(default=0)
    lionsscore5 = models.PositiveSmallIntegerField(default=0)
    firstpoints5 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
    matchpoints5 = models.PositiveSmallIntegerField(default=0)
    sascore6 = models.PositiveSmallIntegerField(default=0)
    lionsscore6 = models.PositiveSmallIntegerField(default=0)
    firstpoints6 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
    matchpoints6 = models.PositiveSmallIntegerField(default=0)
    sascore7 = models.PositiveSmallIntegerField(default=0)
    lionsscore7 = models.PositiveSmallIntegerField(default=0)
    firstpoints7 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
    matchpoints7 = models.PositiveSmallIntegerField(default=0)
    sascore8 = models.PositiveSmallIntegerField(default=0)
    lionsscore8 = models.PositiveSmallIntegerField(default=0)
    firstpoints8 = models.CharField(max_length=20, choices=FIRST_POINTS_SELECT)
    matchpoints8 = models.PositiveSmallIntegerField(default=0)
    points_accrued = models.PositiveSmallIntegerField(default=0)
    
    submit_date = models.DateField(default=datetime.date.today)    

    def __str__(self):
        return self.customer.username
#        return f'{self.id}-{self.customer.username}'