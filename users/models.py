from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

#
# class Owner(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     link = models.ForeignKey('links.Link', related_name='votes', on_delete=models.CASCADE)


class CustomUser(AbstractUser):

    email = models.EmailField(blank=False, max_length=254, verbose_name="email address")

    USERNAME_FIELD = "username"   # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"
