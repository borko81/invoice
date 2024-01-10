from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponse
from decimal import Decimal

from . import models
from . import forms


def new_invoice(request):
    content = {
        "fak_form": forms.FakModelsForm(request.POST or None),
        "produkt_form": forms.FakElModelsForm(request.POST or None),
    }
    if request.method == "GET":
        return render(request, "fak_owner/new_fak.html", content)
    elif request.method == "POST":
        form1 = forms.FakModelsForm(request.POST)
        form2 = forms.FakElModelsForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            python_data = dict(request.POST)
            try:
                fak = form1.save()
                temp_fak_id = models.FakModels.objects.get(fak_number=fak)
                if len(python_data["text"]) > 1:
                    text = python_data["text"]
                    kol = python_data["kol"]
                    dds = python_data["dds"]
                    cena_brutna_ed = python_data["cena_brutna_ed"]
                    total_form2_data = zip(text, kol, dds, cena_brutna_ed)
                    for t, k, d, c in total_form2_data:
                        print(temp_fak_id, t, k, d, c)
                        f2 = models.FakElModels(
                            fak_id=temp_fak_id,
                            text=t,
                            kol=int(k),
                            dds=int(d),
                            cena_brutna_ed=Decimal(c),
                        )
                        f2.save()
                else:
                    f2 = form2.save(commit=False)
                    f2.fak_id = models.FakModels.objects.get(fak_number=fak)
                    f2.save()
            except Exception as er:
                return HttpResponse("Error acquire", str(er))
            else:
                return redirect("fak_owner:invoices")

        return HttpResponse(request.POST)


def invoices(request):
    content = {"invoices": models.FakModels.objects.all()}
    if request.method == "GET":
        return render(request, "fak_owner/fak_lists.html", content)
