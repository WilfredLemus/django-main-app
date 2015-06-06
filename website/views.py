from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import json
from .models import Meal, TypeMeal, Order, OrderMeal, Sell, Call


def index(request):
    # if request.user.is_authenticated():
    #     return redirect("index")
    # else:
    context = {
        'title': 'Restaurant',
        'orders': None
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
        if not request.user.is_anonymous():
            try:
                sells = Sell.objects.filter(user=request.user, is_paid=1).all()
                orders = []
                for sell in sells:
                    orders.append(sell.order)
                context['orders'] = orders
            except Exception:
                pass

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
        a = Call(table_id=username)
        a.save()
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

    try:
        sell = Sell.objects.filter(user=request.user, is_paid=0).get()
    except Exception:
        sell = None

    if sell is None:
        order = None
        total_price = 0
    else:
        order = sell.order
        total_price = order.price

    # your_order = Order.objects.filter(user_id=current_user_id)
    # print(your_order)

    return render(request, "order.html", locals())


def finalize(request):

    user = request.user

    try:
        sell = Sell.objects.filter(user=user, is_paid=0).get()
        order = sell.order
    except Exception:
        return redirect('order')

    content = {
        'order': order
    }
    return render(request, "finalize.html", content)


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

    # current_user_id = request.user.id
    # your_order = Order.objects.filter(user_id=current_user_id)

    # return render(request, "finalize.html", locals())

    else:
        return HttpResponse("You are not allowed to view this page!")

def change_state(request):
    try:
        ord_id = request.GET.get('order_id')
        sell = Sell.objects.get(order=ord_id)
        sell.order.is_served = True
        sell.order.save()
    except Exception:
        return HttpResponse("Nice try....")


def change_state_accepted(request):
    try:
        ord_id = request.GET.get('order_id')
        sell = Sell.objects.get(order=ord_id)
        sell.order.is_accepted = True
        sell.order.save()
    except Exception:
        return HttpResponse("Nice try....")


def change_state_calls(request):
    try:
        ord_id = request.GET.get('table_id')
        print(ord_id)
        Call.objects.filter(table_id=ord_id).delete()
    except Exception:
        return HttpResponse("Nice try....")


def callwaitress(request):
    if request.method == 'POST':
        table = request.POST.get('table')
        call = Call(table_id=table)
        call.save()


def update_order(request):
    if request.method == 'POST':
        order = Order.objects.filter(pk=request.POST.get('order_id'))
        order.is_served = True
        order.save()
        return redirect('get_orders')


def page1(request):
    return render(request, 'page1.html')


def page2(request):
    return render(request, 'page2.html')


def page3(request):
    return render(request, 'page3.html')


def page4(request):
    return render(request, 'page4.html')


def page5(request):
    return render(request, 'page5.html')


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
        return HttpResponse("Wrong URL")

#login required
def get_orders(request):
    sells = Sell.objects.filter(is_paid=0).all()
    tables = Call.objects.all()
    orders = []
    for sell in sells:
        if not sell.order.is_served:
            orders.append(sell.order)
    return render(request, 'admin.html', locals())


def makecurrentorder(request):

    cart = json.loads(request.POST.get("cart"))

    meals = cart['products']
    table_num = request.POST.get("table")
    print(table_num)
    response_data = {
        'success': True
    }

    try:
        sell = Sell.objects.filter(user=request.user, is_paid=0).get()
    except Exception:
        sell = None

    if sell is None:
        order = Order(user_id=request.user, table=table_num, seat_number=0, is_served=0,is_accepted=0)
        order.save()
        Sell(user=request.user, order=order).save()
        order_price = 0
    else:
        order = sell.order
        order_price = order.price

    for meal in meals:
        OrderMeal(meal=Meal.objects.get(pk=meal['real_id']), order=order).save()
        order_price += float(meal["price"])
    order.price = order_price
    order.save()
    return HttpResponse(json.dumps(response_data), content_type="application/json")
