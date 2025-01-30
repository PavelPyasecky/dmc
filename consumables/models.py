from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

from common.db.models import CreatedUpdatedData


class Spares(CreatedUpdatedData):
    name = models.CharField('name', max_length=100)
    count = models.IntegerField('count', validators=[MinValueValidator(1),])
    cost = models.FloatField('cost', validators=[MinValueValidator(0),])
    installation_date = models.DateTimeField('installation_date', default=timezone.now)

    @property
    def total_cost(self):
        return self.count * self.cost


class CompletedWork(CreatedUpdatedData):
    name = models.CharField('name', max_length=100)
    hours = models.IntegerField('hours', validators=[MinValueValidator(0),])
    cost = models.FloatField('cost', validators=[MinValueValidator(0),])
    completed_date = models.DateTimeField('completed_date', default=timezone.now)

    @property
    def total_cost(self):
        return self.count * self.cost
