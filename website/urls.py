from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    # path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("customer/<int:pk>", views.customer_view, name="customer"),
]
