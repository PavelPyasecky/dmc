from django.conf import settings
from django.db import models

from common.db.models import CreatedUpdatedData


class Vehicle(CreatedUpdatedData):
    vin = models.CharField('vin', max_length=20, unique=True)
    country = models.CharField('country', max_length=60, null=True)
    manufacturer = models.CharField('manufacturer', max_length=50, null=True)
    model = models.CharField('model', max_length=50, null=True)
    clas = models.CharField('class', max_length=50, null=True)
    region = models.CharField('region', max_length=50, null=True)
    wmi = models.CharField('wmi', max_length=50, null=True)
    vds = models.CharField('vds', max_length=50, null=True)
    vis = models.CharField('vis', max_length=50, null=True)
    year = models.IntegerField('year', null=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='owner_cars')
