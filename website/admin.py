from django.contrib import admin

from . models import TypeMeal, Meal, Menu, Review


# Register your models here.


admin.site.register(TypeMeal)
admin.site.register(Meal)
admin.site.register(Menu)
admin.site.register(Review)
