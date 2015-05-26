from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    # if request.user.is_authenticated():
    #     return redirect("index")
    # else:
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return redirect("index")
    else:
        return render(request, "index.html")


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

            User.objects.create_user(username, email, password)

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return redirect("index")

        else:
            return render(request, "register.html", locals())


def log(request):
    return render(request, "login.html")
