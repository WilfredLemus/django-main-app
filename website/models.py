from django.db import models

# Create your models here.


class TypeMeal(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)


class Meal(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    price = models.FloatField()
    # type_id = models.ForeignKey(TypeFood)
    # menu_id = models.ManyToManyField(Menu) ??

    def __str__(self):
        return "{} {} {}$".format(self.name, self.rating, self.price)


class Menu(models.Model):
    name = models.CharField(max_length=50)
    # meals = models.ManyToManyField(Meal) ??

    def __str__(self):
        return "{}".format(self.name)


class Review(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # meal = models.ForeignKey(Meal)

    def __str__(self):
        return "{} {}".format(self.content, self.date)


# class Order(models.Model):
#     table = models.PositiveSmallIntegerField()


# class TableMeal(models.Model):
#     pass
