from django.urls import path, include
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
    path('pizzas/<int:pizza_id>/add_photo/', views.add_photo, name='add_photo'),
    path('pizzas/<int:pizza_id>/assoc_ingredient/<int:ingredient_id>/', views.assoc_ingredient, name='assoc_ingredient'),
    path('pizzas/<int:pizza_id>/unassoc_ingredient/<int:ingredient_id>/', views.unassoc_ingredient, name='unassoc_ingredient'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredients_index'),
    path('ingredients/<int:pk>/', views.IngredientDetail.as_view(), name='ingredients_detail'),
    path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredients_create'),
    path('ingredients/<int:pk>/update/', views.IngredientUpdate.as_view(), name='ingredients_update'),
    path('ingredients/<int:pk>/delete/', views.IngredientDelete.as_view(), name='ingredients_delete'),
     path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),


]