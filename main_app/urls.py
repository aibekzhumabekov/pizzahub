from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('about/', views.about, name='about'),
      # route for pizzas index
    path('pizzas/', views.pizzas_index, name='index')
]