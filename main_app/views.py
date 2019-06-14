from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pizza, Ingredient
from .forms import OrderForm


# Define the home view
class PizzaCreate(CreateView):
  model = Pizza
  fields = '__all__'
  success_url = '/pizzas/'

class PizzaUpdate(UpdateView):
  model = Pizza
  # Let's make it impossible to rename a pizza :)
  fields = ['name', 'descriptions', 'pizzeria', 'country']

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
  order_form = OrderForm()
  return render(request, 'pizzas/detail.html', {
     'pizza': pizza, 'order_form': order_form 
    })

def add_order(request, pizza_id):
	# create the ModelForm using the data in request.POST
  form = OrderForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the pizza_id assigned
    new_order = form.save(commit=False)
    new_order.pizza_id = pizza_id
    new_order.save()
  return redirect('detail', pizza_id=pizza_id)

class IngredientList(ListView):
  model = Ingredient

class IngredientDetail(DetailView):
  model = Ingredient

class IngredientCreate(CreateView):
  model = Ingredient
  fields = '__all__'

class IngredientUpdate(UpdateView):
  model = Ingredient
  fields = ['name', 'color']

class IngredientDelete(DeleteView):
  model = Ingredient
  success_url = '/Ingredients/'