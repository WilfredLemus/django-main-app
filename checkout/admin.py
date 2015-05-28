from django.contrib import admin
from . models import userStripe

# Register your models here.


class userStripeAdmin(admin.ModelAdmin):

    class Meta:
        model = userStripe

admin.site.register(userStripe, userStripeAdmin)
