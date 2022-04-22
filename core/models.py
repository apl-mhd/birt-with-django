import email
from unicodedata import name
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=32, null=True)
    email =models.CharField(max_length=32, null=True)
    phone =models.CharField(max_length=32, null=True)


    def __str__(self):
        return self.name
    