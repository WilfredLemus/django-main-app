from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register/$', views.register, name="register"),
    url(r"^logout/$", views.user_logout, name="logout"),
    url(r"^login/$", views.log, name="log"),
    url(r"^order/$", views.order, name="order"),
    url(r"^callwaiter/$", views.callwaiter, name="callwaiter"),
    url(r"^page1/$", views.page1, name="page1"),
    url(r"^search/$", views.search, name="search"),
    url(r"^get_orders/$", views.get_orders, name="get_orders"),
    url(r"^order/finalize/$", views.finalize, name="finalize"),
]
