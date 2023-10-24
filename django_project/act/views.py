from datetime import datetime
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from act.models import User

# Create your views here.
def login_page(request):
    user=None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
    if user is not None:
        login(request, user)
        return render(request, "hello/home.html")
    else: return render(request, "hello/login.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
            password = password
        )
        user.save()
        return render(request, 'hello/register.html')
    else: return render(request, 'hello/register.html')

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


def home(request):
    return render(request, "hello/home.html")

def information(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, "hello/information.html", context)

def contact(request):
    return render(request, "hello/contact.html")
