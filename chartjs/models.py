from django.db import models

# Create your models here.
class Company(models.Model):
    symbol = models.CharField(max_length=120)
    rank = models.PositiveIntegerField()
    date = models.DateField()