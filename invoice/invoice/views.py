from django.shortcuts import render, redirect
from django.contrib.auth import logout


def check_base(request):
    return render(request, "fak_owner/base.html", {})


def logout_view(request):
    logout(request)
    return redirect("login")
