from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



from orders.models import Order ,Regular_Pizza , Sicilian_Pizza, Toppings, Subs, Pasta, Salads, Dinner_Platters

# Create your views here.
#def index(request):
#    return HttpResponse("Project 3: TODO")


# Create your views here.


def menu_view(request):

    rp = Regular_Pizza.objects.all()
    sp = Sicilian_Pizza.objects.all()
    tp = Toppings.objects.all()
    sb = Subs.objects.all()
    ps = Pasta.objects.all()
    sl = Salads.objects.all()
    dp = Dinner_Platters.objects.all()

    

    context = {'Regular_Pizza':rp,  'Sicilian_Pizza':sp, 'Toppings':tp, 'Subs':sb, 'Pasta':ps, 'Salads':sl, 'Dinner_Platters':dp}
    return render(request, 'orders/menu.html', context)


def menu_order(request):

    print('hihihi')
    menus = request.POST['menus']
    topping = request.POST['topping']
    price = request.POST['price'] 
    print(menus)
    print(topping)
    print(price)

    o = Order(menus=menus , topping=topping, price=price)
    o.save()
    return menu_view(request)