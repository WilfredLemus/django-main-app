from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
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

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
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

def callwaiter(request):
    if request.method == "POST":
        username = request.POST.get("table")
        print(username)
        return HttpResponse("dadadada")


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
            return render(request, "index.html", locals())


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
    print(current_user_id)

    your_order = Order.objects.filter(user_id=current_user_id, is_paid=False)
    print(your_order)

    # bam = your_order.get_meals()
    # print (bam)
    return render(request, "order.html", locals())


def finalize(request):

    if request.method == "POST":
        user = request.user
        meal_id = int(request.POST.get("meal_id"))
        print(type(meal_id))
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


def search(request):
    if request.method == 'POST' or request.method == "GET":
        data = request.POST.get("meal")
        print(data)
        meals = Meal.objects.filter(name__icontains=data)
        if meals:
            data = meals
        else:
            return HttpResponse("No meals found!")
        return render(request,'meals.html', locals())

    else:
        return HttpResponse("You are not allowed to view this page!")

#login required
def update_order(request):
    if request.method == 'POST':
        order = Order.objects.filter(pk=request.POST.get('order_id'))
        order.is_served = True
        order.save()
        return redirect('get_orders')

#login required
def get_orders(request):
    if request.method == 'GET':
        drinks=Order.objects.filter(meals__type_id__name='drinks', is_paid=False).order_by('table')
        kitchen = Order.objects.exclude(meals__type_id__name='drinks', is_paid=False).order_by('table')
        for order in drinks:
            print("{} {} {} {}".format(order.seat_number,
                                       order.table,
                                       order.date,
                                       type(order.meals)))
        return HttpResponse("Bllalaalal")
    else:
        pass


