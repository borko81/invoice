from django.shortcuts import render


def check_base(request):
    return render(request, "fak_owner/base.html", {})
