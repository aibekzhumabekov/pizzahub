from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=250)
    pizzeria = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name