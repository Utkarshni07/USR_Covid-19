from django.db import models
from django import forms


# Create your models here.


class CovidData(models.Model):
    DryCough = models.FloatField()
    HighFever = models.FloatField()
    SoreThroat = models.FloatField()
    Difficulty_in_breathing = models.FloatField()
    Infected_with_Covid19 = models.FloatField()


class Coviduser(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=67)
    password = models.CharField(max_length=67)
    username = models.CharField(max_length=89)


class contact(models.Model):
    username = models.CharField(max_length=145)
    email = models.EmailField()
    message = models.TextField()

