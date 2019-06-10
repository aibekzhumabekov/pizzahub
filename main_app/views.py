from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Add the Pizza class & list and view function below the imports
class Pizza:
    def __init__(self, name, ingredients, pizzeria, country):
        self.name = name
        self.ingredients = ingredients
        self.pizzeria = pizzeria
        self.country = country

pizzas = [
    Pizza('Rhode Island', 'N/A', 'Figidini', 'USA'),
    Pizza('Copenhagen', 'N/A', 'Mother', 'Denmark'),
    Pizza('Di Farra Pizza', 'N/A', 'Di Fara', 'New York, USA')
    
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
def about(request):
  return render(request, 'about.html')
  # Add new view
def pizzas_index(request):
    return render(request, 'pizzas/index.html', { 'pizzas': pizzas })