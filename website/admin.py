from django.contrib import admin

from . models import TypeMeal, Meal, Review, Order, OrderMeal, Sell, Call



# Register your models here.


admin.site.register(TypeMeal)
admin.site.register(Meal)
admin.site.register(Review)
admin.site.register(Order)

admin.site.register(OrderMeal)
admin.site.register(Sell)
admin.site.register(Call)
