from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import uuid
import boto3
from .models import Pizza, Ingredient, Photo
from .forms import OrderForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollectapp'

class PizzaCreate(CreateView):
  model = Pizza
  fields = ['name', 'descriptions', 'pizzeria', 'country']
  success_url = '/pizzas/'

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class PizzaUpdate(UpdateView):
  model = Pizza
  fields = ['name', 'descriptions', 'pizzeria', 'country']

class PizzaDelete(DeleteView):
  model = Pizza
  success_url = '/pizzas/'

def home(request):
  return render(request, 'home.html')
  
def about(request):
  return render(request, 'about.html')
  # Add new view
@login_required
def pizzas_index(request):
  pizzas = Pizza.objects.filter(user=request.user)
  return render(request, 'pizzas/index.html', { 'pizzas': pizzas })
@login_required

def pizzas_detail(request, pizza_id):
  pizza = Pizza.objects.get(id=pizza_id)
  ingredients_pizza_doesnt_have = Ingredient.objects.exclude(id__in = pizza.ingredients.all().values_list('id'))
  order_form = OrderForm()
  return render(request, 'pizzas/detail.html', {
     'pizza': pizza, 'order_form': order_form,
     'ingredients': ingredients_pizza_doesnt_have
    })


@login_required
def add_order(request, pizza_id):
  form = OrderForm(request.POST)
  if form.is_valid():
    new_order = form.save(commit=False)
    new_order.pizza_id = pizza_id
    new_order.save()

  return redirect('detail', pizza_id=pizza_id)
@login_required
def add_photo(request, pizza_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to pizza_id or pizza (if you have a pizza object)
            photo = Photo(url=url, pizza_id=pizza_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', pizza_id=pizza_id)
@login_required
def assoc_ingredient(request, pizza_id, ingredient_id):
  Pizza.objects.get(id=pizza_id).ingredients.add(ingredient_id)
  return redirect('detail', pizza_id=pizza_id)
@login_required
def unassoc_ingredient(request, pizza_id, toy_id):
  Pizza.objects.get(id=pizza_id).toys.remove(toy_id)
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
  success_url = '/ingredients'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)