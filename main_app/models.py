from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

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

  def order_for_today(self):
    return self.order_set.filter(date=date.today()).count() >= len(MEALS)

class Order(models.Model):
  date = models.DateField('order date')
  meal = models.CharField(
  max_length=1,
  choices=MEALS,
  default=MEALS[0][0]
  )
  pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

