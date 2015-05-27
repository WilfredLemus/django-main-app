from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Meal, TypeMeal, Order


def index(request):
    # if request.user.is_authenticated():
    #     return redirect("index")
    # else:
    context = {
        'title': 'Restaurant'
    }
    print(request.user)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        print("Tup")
        print(user)
        if user is not None:
            print("Kurva")
            login(request, user)
            return redirect("index")
        else:
            return redirect('index')
    else:
        return render(request, "index.html", context)


def _validate_register(username, email, password, password2):
    if username is None or username.strip() == "":
        return False

    if email is None or email.strip() == "":
        return False

    if password is None or password.strip() == "" or password != password2:
        return False

    return True


def user_logout(request):
    logout(request)
    return redirect("index")


def register(request):

    if request.user.is_authenticated():
        return redirect("index")

    else:

        if request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            password2 = request.POST.get("password2")

            if not _validate_register(username, email, password, password2):
                return redirect("register")

            user = User.objects.create_user(username, email, password)

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return redirect("index")

        else:
            return render(request, "register.html", locals())


def log(request):
    return render(request, "login.html")


def order(request):

    meals = Meal.objects.all()

    types = TypeMeal.objects.all()

    type_meals = {}

    # for i in types:
    #     meals = Meal.objects.filter(type_id=i.id)
    #     type_meals[i] = meals

    current_user_id = request.user.id
    print (current_user_id)

    your_order = Order.objects.filter(user_id=current_user_id, is_paid=False)
    print (your_order)

    # bam = your_order.get_meals()
    # print (bam)
    return render(request, "order.html", locals())


def finalize(request):

    if request.method == "POST":
        user = request.user
        meal_id = int(request.POST.get("meal_id"))
        print (type(meal_id))
        table_number = int(request.POST.get("table_number"))

        meal = Meal.objects.filter(id=meal_id).first()

        pam = Order.objects.create(
            user_id=user,
            is_paid=False,
            table=table_number,
        )
        pam.save()

        pam.meals.add(meal)
        pam.save()


    return render(request, "finalize.html")
