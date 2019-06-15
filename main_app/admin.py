from django.contrib import admin
from .models import Pizza, Order, Ingredient, Photo
# Register your models here.

admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(Ingredient)
admin.site.register(Photo)