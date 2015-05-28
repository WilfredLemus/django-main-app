from django.shortcuts import render
import stripe
from django.contrib.auth.decorators import login_required

from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def checkout(request):
    publishKey = settings.STRIPE_SECRET_KEY
    context = {}

    customer_id = request.user.userstripe.stripe_id
    print(customer_id)

    if request.method == "POST":
        token = request.POST['stripeToken']

        customer = stripe.Customer.retrieve(customer_id)
        customer.cards.create(token)


        # Set your secret key: remto your live secret key in production
        # See your keys here https://dashboard.stripe.com/account/apikeys
        stripe.api_key = "sk_test_dAIMPSAPAuWf8RAmypa0sDVf"
        print(request.POST['price'])
        price = int(request.POST['price'])
        price *= 100

        charge = stripe.Charge.create(
            amount=price,
            currency="usd",
            customer=customer,
            source=token,
            description="Example charge"
        )
        context['success'] = 'You paid successully!'

    return render(request, "checkout.html", context)
