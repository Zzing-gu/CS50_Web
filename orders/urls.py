from django.urls import path

from . import views


app_name = 'orders'
urlpatterns = [
    path("menu_view", views.menu_view, name="menu_view"),
    path("menu_order", views.menu_order, name="menu_order"),
]
