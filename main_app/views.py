from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pizza


# Define the home view
class PizzaCreate(CreateView):
  model = Pizza
  fields = '__all__'
  success_url = '/pizzas/'

class PizzaUpdate(UpdateView):
  model = Pizza
  # Let's make it impossible to rename a pizza :)
  fields = ['name', 'ingredients', 'pizzeria', 'country']

class PizzaDelete(DeleteView):
  model = Pizza
  success_url = '/pizzas/'

# class PizzaCreate(CreateView):
#   model = Pizza
#   fields = ['name', 'ingredients', 'pizzeria', 'country']

def home(request):
  return render(request, 'home.html')
  
def about(request):
  return render(request, 'about.html')
  # Add new view
def pizzas_index(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizzas/index.html', { 'pizzas': pizzas })

def pizzas_detail(request, pizza_id):
  pizza = Pizza.objects.get(id=pizza_id)
  return render(request, 'pizzas/detail.html', { 'pizza': pizza })

