from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register/$', views.register, name="register"),
    url(r"^logout/$", views.user_logout, name="logout"),
    url(r"^login/$", views.log, name="log"),
    url(r"^order/$", views.order, name="order"),
    url(r"^search/$", views.search, name="search"),
    url(r"^callwaitress/$", views.callwaitress, name="callwaitress"),
    url(r"^change_state_accepted/", views.change_state_accepted, name="change_state_accepted"),
    url(r"^change_state_calls/", views.change_state_calls, name="change_state_calls"),
    url(r"^change_state/", views.change_state, name="change_state"),
    url(r"^get_orders/$", views.get_orders, name="get_orders"),
    url(r"^order/finalize/$", views.finalize, name="finalize"),
    url(r"^order/makecurrentorder/$", views.makecurrentorder, name="makecurrentorder"),
]
