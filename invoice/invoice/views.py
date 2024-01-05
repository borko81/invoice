from django.shortcuts import render


def check_base(request):
    return render(request, "base.html", {})
