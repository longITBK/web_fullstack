from datetime import datetime
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import generic

from act.models import *

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

# def home(request):
#     return HttpResponse("Hello, Django!")

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

# This class extends from django generic Views
class HomeView(generic.TemplateView):
    template_name = "hello/home.html"

# def home(request):
#     return render(request, "hello/home.html")

  
def building(request):
    buidlings = Building.objects.all()
    context = {
        'buildings': buidlings
    }
    return render(request, "hello/building.html", context)

def create_building(request):
    if request.method == "POST":
        form = BuildingForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                return redirect('/building/')
            except: 
                pass
    return render(request, "hello/create_building.html")

def update_building(request, id):
    if request.method == "POST":
        building = Building.objects.get(id = id)
        form = BuildingForm(request.POST, instance=building)
        if form.is_valid:
                try:
                    form.save()
                    return redirect('/building/')
                except: 
                    pass
    building = Building.objects.get(id = id)
    return render(request, "hello/update_building.html", {'building' : building})

def delete_building(request, id):
    building = Building.objects.get(id = id)
    building.delete()
    return redirect('/building/')




# This class extends from django generic Views
class ContactView(generic.ListView):
    model = Room
    template_name = "hello/room.html"
    context_object_name = 'rooms'

# def contact(request):
#     names = User.objects.all()
#     context = {'names': names}
#     return render(request, "hello/contact.html", context=context)
