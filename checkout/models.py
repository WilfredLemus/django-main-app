from django.db import models

# import stripe

# from django.conf import settings

# from allauth.account.signals import user_logged_in
# from django.contrib.auth.models import User


# stripe.api_key = settings.STRIPE_SECRET_KEY


# class userStripe(models.Model):
#     user = models.OneToOneField(User)
#     stripe_id = models.CharField(max_length=200, null=True, blank=True)

#     # def __unicode__(self):
#     #     if self.stripe_id:
#     #         return str(self.stripe_id)
#     #     else:
#     #         return self.user.username


# def stripeCallback(sender, request, user, **kwargs):
#     user_stripe_account, created = userStripe.objects.get_or_create(user=user)

#     if created:
#         print("created for {}".format(user.username))

#     if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
#         new_stripe_id = stripe.Customer.create(email=user.email)

#         print("------ {}".format(new_stripe_id))

#         user_stripe_account.stripe_id = new_stripe_id["id"]
#         user_stripe_account.save()


# user_logged_in.connect(stripeCallback)
