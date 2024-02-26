from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        #remove this!
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, "accounts/login.html", context)
        login(request, user)
        return redirect('/admin')
    return render(request, "accounts/login.html", {})

def logout_view(request):

    return render(request, "accounts/login.html", {})


def register_view(request):

    return render(request, "accounts/login.html", {})