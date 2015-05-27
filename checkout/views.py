from django.shortcuts import render
import stripe
from django.contrib.auth.decorators import login_required


@login_required
def checkout(request):
    context = {}
    if request.method == "POST":
        # Set your secret key: remto your live secret key in production
        # See your keys here https://dashboard.stripe.com/account/apikeys
        stripe.api_key = "sk_test_dAIMPSAPAuWf8RAmypa0sDVf"
        token = request.POST['stripeToken']
        print(request.POST['price'])
        price = int(request.POST['price'])
        price *= 100

        charge = stripe.Charge.create(amount=price, currency="usd", source=token, description="Example charge")
        context['success'] = 'You paid successully!'

    return render(request, "checkout.html", context)
