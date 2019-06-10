from django.shortcuts import render
from .models import Pizza


# Define the home view
def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')
  # Add new view
def pizzas_index(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizzas/index.html', { 'pizzas': pizzas })