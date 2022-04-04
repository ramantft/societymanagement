from enum import unique
from django.db import models


class Userotp(models.Model):
    def __str__(self):
        return self.otp
    email = models.CharField(max_length=200, null=False)
    otp = models.CharField(max_length = 4)
    is_verified = models.BooleanField(default=False)

class Userprofile(models.Model):
    def __str__(self):
        return self.email
    email = models.CharField(max_length=200, null=False)
    username = models.CharField(max_length=200, null=False)
    flat_no = models.CharField(max_length=200, null=False)
    tower_no = models.CharField(max_length=200, null=False)