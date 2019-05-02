from django.contrib import admin

from .models import Regular_Pizza, Sicilian_Pizza, Toppings, Subs, Pasta, Salads, Dinner_Platters 
# Register your models here.

admin.site.register(Regular_Pizza)
admin.site.register(Sicilian_Pizza)
admin.site.register(Toppings)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(Dinner_Platters)