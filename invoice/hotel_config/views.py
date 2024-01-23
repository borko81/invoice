from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from . import models
from . import forms


@login_required
def floors(request):
    context = {"title": "Етажи", "all_floors": models.FloorsModel.objects.all()}
    return render(request, "config/floors.html", context)


@login_required
def new_floor(request):
    if request.method == "POST":
        name = request.POST.get("name")
        models.FloorsModel.objects.create(name=name)
    return redirect("hotel:floors")


@login_required
def delete_floor(request, id_):
    floor = get_object_or_404(models.FloorsModel, id=id_)
    floor.delete()
    return redirect("hotel:floors")


@login_required
def edit_floor(request, id_):
    form = forms.FloorForm(
        request.POST or None, instance=models.FloorsModel.objects.get(id=id_) or None
    )
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("hotel:floors")
    return render(
        request,
        "config/edit_floor.html",
        {
            "form": form,
        },
    )


# Beds
@login_required
def beds(request):
    form = forms.BedsForm(request.POST or None)
    context = {
        "title": "Легла",
        "all_beds": models.BedsModel.objects.all(),
        "form": form,
    }
    return render(request, "config/beds.html", context)


@login_required
def new_bed(request):
    form = forms.BedsForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("hotel:beds")
    return render(request, "config/beds.html", context)


@login_required
def delete_bed(request, id_):
    floor = get_object_or_404(models.BedsModel, id=id_)
    floor.delete()
    return redirect("hotel:beds")


@login_required
def edit_bed(request, id_):
    form = forms.FloorForm(
        request.POST or None, instance=models.FloorsModel.objects.get(id=id_) or None
    )
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("hotel:beds")
    return render(
        request,
        "config/edit_bed.html",
        {
            "form": form,
        },
    )
