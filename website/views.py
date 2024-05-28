from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Welcome! You have been logged In!")
            return redirect("homepage")
        else:
            messages.success(
                request, "There was an error logging in! Please try again!"
            )
            return redirect("homepage")
    else:
        return render(request, "home.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect("homepage")

def register_user(request):
    return render(request, 'register.html', {})