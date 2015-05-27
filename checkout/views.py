from django.shortcuts import render
import stripe
from django.contrib.auth.decorators import login_required


@login_required
def checkout(request):
    if request.method == "POST":
        # Set your secret key: remto your live secret key in production
        # See your keys here https://dashboard.stripe.com/account/apikeys
        stripe.api_key = "sk_test_dAIMPSAPAuWf8RAmypa0sDVf"
        token = request.POST['stripeToken']

        charge = stripe.Charge.create(amount=1500, currency="usd", source=token, description="Example charge")

    context = {}
    return render(request, "checkout.html", context)
