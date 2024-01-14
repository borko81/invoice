from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
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


def delete_fak(request, id_):
    fak = get_object_or_404(models.FakModels, fak_number=id_)
    fak.is_deleted = True
    fak.save()
    content = {"invoices": models.FakModels.objects.all()}
    return render(request, "fak_owner/fak_lists.html", content)


def edit_invoice(request, id_: str):
    temp_fak_id = models.FakModels.objects.get(fak_number=id_)
    temp_fak_elements = models.FakElModels.objects.filter(fak_id=temp_fak_id)
    fak_form = forms.FakModelsForm(request.POST or None, instance=temp_fak_id or None)
    content = {
        "fak_id": temp_fak_id,
        "fak_elemets": temp_fak_elements,
        "fak_form": fak_form,
        "produkt_form": forms.FakElModelsForm(request.POST or None),
    }
    if request.method == "GET":
        return render(request, "fak_owner/edit_fak.html", content)
    elif request.method == "POST":
        if fak_form.is_valid():
            fak_form.save()
            temp_products_id = request.POST.getlist("product_id")
            for temp_product_id in temp_products_id:
                temp_product = models.FakElModels.objects.get(id=int(temp_product_id))
                print(temp_product)

            return redirect("fak_owner:invoices")

    return HttpResponse(request.POST)


def delete_product_row(request, id_):
    if request.method == "DELETE":
        product_row = get_object_or_404(models.FakElModels, id=int(id_))
        invoice_number = product_row.fak_id
        product_row.delete()

        temp_fak_id = models.FakModels.objects.get(fak_number=invoice_number)
        temp_fak_elements = models.FakElModels.objects.filter(fak_id=temp_fak_id)
        fak_form = forms.FakModelsForm(
            request.POST or None, instance=temp_fak_id or None
        )
        content = {
            "fak_id": temp_fak_id,
            "fak_elemets": temp_fak_elements,
            "fak_form": fak_form,
            "produkt_form": forms.FakElModelsForm(request.POST or None),
        }

        return render(request, "fak_owner/edit_fak.html", content)


def show_invoice(request, id_):
    current_invoice = get_object_or_404(models.FakModels, id=id_)
    owner = models.Owner.objects.all()[0]
    client = models.Client.objects.get(id=current_invoice.client.id)
    products = models.FakElModels.objects.filter(fak_id=id_)
    content = {
        "title": current_invoice.fak_number,
        "current_invoice": current_invoice,
        "owner": owner,
        "client": client,
        "products": products,
    }
    return render(request, "fak_owner/show_invoice.html", content)
