from django.db import models
from django.contrib.auth.models import User


class TypeMeal(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)


class Meal(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    price = models.FloatField()
    description = models.TextField(default="")
    image = models.ImageField()
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
            self.user_id, self.content, self.date, self.meal)


class Call(models.Model):
    table_id = models.PositiveSmallIntegerField()


class Order(models.Model):
    user_id = models.ForeignKey(User)
    seat_number = models.PositiveSmallIntegerField()
    price = models.FloatField(default=0)
    table = models.PositiveSmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    # is_paid = models.BooleanField()
    is_served = models.BooleanField()
    is_accepted = models.BooleanField()


    def get_price(self):
        return sum([meal.price for meal in self.meals.all()])

    def get_meals(self):
        return [meal for meal in self.meals.all()]

    def get_meals_printable(self):
        meals = self.ordermeal_set.all()
        all_meals = []
        meals_set = set()
        for meal in meals:
            all_meals.append(meal.meal.name)
        for meal in all_meals:
            meals_set.add("{} x{}".format(meal, all_meals.count(meal)))
        return ",".join(meals_set)


class Sell(models.Model):
    user = models.ForeignKey(User)
    order = models.ForeignKey(Order)
    is_paid = models.BooleanField(default=0)


class OrderMeal(models.Model):
    meal = models.ForeignKey(Meal)
    order = models.ForeignKey(Order)
