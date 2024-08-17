from django.conf import settings
from django.db import models


class CreatedUpdatedData(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                   related_name="created_%(class)s_related",
                                   related_query_name="created_%(class)s")
    created_date = models.DateTimeField('created_date', auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                   related_name="updated_%(class)s_related",
                                   related_query_name="updated_%(class)s")
    updated_date = models.DateTimeField('updated_date', auto_now=True)

    class Meta:
        abstract = True
