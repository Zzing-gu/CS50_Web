from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
#def index(request):
#    return HttpResponse("Project 3: TODO")


# Create your views here.
def index(request):
    context = {'hihi':9999}
    return render(request, 'orders/index.html',context)

def register_view(request):
    context = {'hihi':9999}
    return render(request, 'orders/register.html', context)

def register_action(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        first = request.POST["first_name"]
        last = request.POST["last_name"]
        email = request.POST["email_address"]
        if username and password and first and last and email:
            print('savesavesaved')
            user = User.objects.create_user(username,email,password)
            user.save()
            print(username)
    return render(request, 'orders/index.html')

def login_view(request):
    context = {'hihi':9999}
    return render(request, 'orders/login.html', context)

def menu_view(request):
    context = {'hihi':9999}
    return render(request, 'orders/menu.html', context)

def login_action(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print('logged in!!')
        return render(request, 'orders/index.html', {"message":"logged in!"})
    else:
        return render(request, 'orders/login.html', {"message":"invalid credential"})


def logout_action(request):
    logout(request)
    return render(request, "orders/index.html", {"message":"Logged out."})