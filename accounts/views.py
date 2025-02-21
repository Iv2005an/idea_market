from django.shortcuts import render, redirect
from django.contrib.auth import login
from accounts.forms import RegisterForm


def register(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "registration/register.html", {"form": form})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, "registration/register.html", {"form": form})
