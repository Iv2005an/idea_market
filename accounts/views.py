from django.shortcuts import render, redirect
from accounts.forms import RegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "GET":
        form = RegisterForm()
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "registration/profile.html")


@login_required
def my_ideas(request):
    return render(request, "registration/ideas.html")
