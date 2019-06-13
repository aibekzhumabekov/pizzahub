from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pizzas/', views.pizzas_index, name='index'),
    path('pizzas/<int:pizza_id>/', views.pizzas_detail, name='detail'),
    path('pizzas/create/', views.PizzaCreate.as_view(), name='pizzas_create'),
    path('pizzas/<int:pk>/update/', views.PizzaUpdate.as_view(), name='pizzas_update'),
    path('pizzas/<int:pk>/delete/', views.PizzaDelete.as_view(), name='pizzas_delete'),
    path('pizzas/<int:pizza_id>/add_order/', views.add_order, name='add_order'),
 
]