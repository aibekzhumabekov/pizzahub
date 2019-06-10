from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pizzas/', views.pizzas_index, name='index'),
    path('pizzas/<int:pizza_id>/', views.pizzas_detail, name='detail'),
]