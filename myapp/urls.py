from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name ="home"),
    path("home/", views.home, name="home"),
    path("checkers/", views.checkers, name="checkers"),
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name ="login"),
    path("logout/", views.logOutUser, name ="logout"),
]