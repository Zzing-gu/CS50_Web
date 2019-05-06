from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Regular_Pizza

# Create your views here.
#def index(request):
#    return HttpResponse("Project 3: TODO")


# Create your views here.


def menu_view(request):

    r = Regular_Pizza.objects.all()


    print(r)

    context = {'hihi':r}
    return render(request, 'orders/menu.html', context)

