from django.shortcuts import render
import stripe
from django.contrib.auth.decorators import login_required
from website.models import Order
from django.conf import settings


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

    print(request.user.id)

    if request.method == "POST":
        token = request.POST['stripeToken']

        # customer = stripe.Customer.retrieve(customer_id)
        # customer.cards.create(card=token)


        # Set your secret key: remto your live secret key in production
        # See your keys here https://dashboard.stripe.com/account/apikeys
        stripe.api_key = "sk_test_2S6OntzC28nv98hcy3Wtd81I"
        order = Order.objects.get(id=id)
        price = int(order.get_price()) * 100

        charge = stripe.Charge.create(
            amount=price,
            currency="usd",
            source=token,
            description="Example charge"
        )
        context['success'] = 'You paid successully!'

    return render(request, "checkout.html", context)
