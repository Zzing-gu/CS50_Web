from django.urls import path

from . import views


app_name = 'orders'
urlpatterns = [
    path("menu_view", views.menu_view, name="menu_view"),
]
