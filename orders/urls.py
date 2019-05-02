from django.urls import path

from . import views


app_name = 'orders'
urlpatterns = [
    path("", views.index, name="index"),
    path("register_view", views.register_view, name="register_view"),
    path("register_action", views.register_action, name="register_action"),
    path("login_view", views.login_view, name="login_view"),
    path("login_action", views.login_action, name="login_action"),
    path("logout_action", views.logout_action, name="logout_action"),
]
