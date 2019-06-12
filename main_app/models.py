from django.db import models
from django.urls import reverse

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=300)
    pizzeria = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pizza_id': self.id})