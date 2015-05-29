from django.shortcuts import render, redirect
import stripe
from django.contrib.auth.decorators import login_required
from website.models import Order
from django.conf import settings

from website.models import Sell



stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request, id):
    publishKey = settings.STRIPE_PUBLIC_KEY
    context = {}
    # print(request.user)
    # customer_id = request.user.id
    # customer_id = request.user.userstripe.stripe_id
    # print(request.user.userstripe)
    # print(customer_id)

    # print("user_id: {}".format(request.user.id))
    # print("order_id: {}".format(id))

    success = False
    if request.method == "POST":
        token = request.POST['stripeToken']

        # customer = stripe.Customer.retrieve(customer_id)
        # customer.cards.create(card=token)

        # Set your secret key: remto your live secret key in production
        # See your keys here https://dashboard.stripe.com/account/apikeys
        stripe.api_key = "sk_test_2S6OntzC28nv98hcy3Wtd81I"
        order = Order.objects.get(id=id)
        # price = int(order.get_price()) * 100

        order_meals = list(order.ordermeal_set.all())
        order_price = 0
        for order_meal in order_meals:
            order_price += order_meal.meal.price

        order_price *= 100
        context = {}
        # context['success'] = 'Try again'
        success = False
        try:
            charge = stripe.Charge.create(
                amount=int(order_price),
                currency="usd",
                source=token,
                description="Example charge"
            )
            # context['success'] = 'You paid successully!'
            success = True
        except:
            success = False
            # context['success'] = 'Try again'

        sell = Sell.objects.filter(order=order).get()
        sell.is_paid = True
        sell.save()

    if success:
        success_message = "You paid your bill successully!"
        return redirect("index")
    else:
        return render(request, "checkout.html", locals())
