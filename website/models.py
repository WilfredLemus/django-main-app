from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class TypeMeal(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)


class Meal(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    price = models.FloatField()
    description = models.TextField(default="")
    # image = models.ImageField()
    type_id = models.ForeignKey(TypeMeal)
    # menu_id = models.ManyToManyField(Menu) ??

    def __str__(self):
        return "{} {} {}$".format(self.name, self.rating, self.price)


# class Menu(models.Model):
#     name = models.CharField(max_length=50)
#     # meals = models.ManyToManyField(Meal) ??

#     def __str__(self):
#         return "{}".format(self.name)


class Review(models.Model):
    user_id = models.ForeignKey(User)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    meal_id = models.ForeignKey(Meal)

    def __str__(self):
        return "{} {} {} {}".format(
            self.user_id, self.content, self.date, self.meal
                                    )


class Order(models.Model):
    user_id = models.ForeignKey(User)
    seat_number = models.PositiveSmallIntegerField()
    table = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    meals = models.ManyToManyField(Meal, related_name='all_meals')
    is_paid = models.BooleanField()
    is_served = models.BooleanField()

    # def __str__(self):
    #     result = ("{} {} {}\n".format(self.user_id, self.table, self.date))

    #     for meal in self.meals.all():
    #         result += "{}\n".format(str(meal))
    #     return result

    def get_meals(self):
        return [meal for meal in self.meals.all()]
