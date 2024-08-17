from django.core.validators import MinValueValidator
from django.db import models

from common.db.models import CreatedUpdatedData


class Spares(CreatedUpdatedData):
    name = models.CharField('name', max_length=100)
    count = models.IntegerField('count', validators=[MinValueValidator(1),])
    cost = models.FloatField('cost', validators=[MinValueValidator(0),])

    @property
    def total_cost(self):
        return self.count * self.cost


class CompletedWork(CreatedUpdatedData):
    name = models.CharField('name', max_length=100)
    hours = models.IntegerField('hours', validators=[MinValueValidator(0),])
    cost = models.FloatField('cost', validators=[MinValueValidator(0),])

    @property
    def total_cost(self):
        return self.count * self.cost
