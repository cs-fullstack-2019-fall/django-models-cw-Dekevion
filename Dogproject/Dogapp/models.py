from django.db import models

# Create your models here.
from django.db import models


class Dog(models.Model):
    dogName = models.CharField(max_length=200)
    dogBreed = models.CharField(max_length=200)
    dogColor = models.CharField(max_length=200)
    dogGender = models.CharField(max_length=200)


class Account(models.Model):
    userName = models.CharField(max_length=200)
    realName = models.CharField(max_length=200)
    accountNumber = models.IntegerField
    balance = models.DecimalField(max_digits=10, decimal_places=3)




