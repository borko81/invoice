from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages

from . import models
from . import forms


# Bank account create, update, delete and list
class OwnerBankListView(ListView):
    template_name = "fak_owner/ownerbank_list.html"
    model = models.OwnerBank

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "BankAccount"
        return context


class OwnerBanNew(CreateView):
    template_name = "fak_owner/ownerbank_list.html"
    model = models.OwnerBank
    form_class = forms.OwnerBankForm

    def get_context_data(self, **kwargs):
        context = super(OwnerBanNew, self).get_context_data(**kwargs)
        context["title"] = "NewBankAccount"
        context["create"] = True
        return context

    def get_success_url(self):
        messages.success(self.request, "Успешен запис")
        return reverse("fak_owner:bank_list")


class OwnerBankEdit(UpdateView):
    template_name = "fak_owner/ownerbank_list.html"
    model = models.OwnerBank
    form_class = forms.OwnerBankForm

    def get_success_url(self):
        messages.success(self.request, "Успешена редакция")
        return reverse("fak_owner:bank_list")

    def get_context_data(self, **kwargs):
        context = super(OwnerBankEdit, self).get_context_data(**kwargs)
        context["title"] = "NewBankAccount"
        context["edit"] = True
        return context


class OwnerBankDelete(DeleteView):
    template_name = "fak_owner/ownerbank_list.html"
    model = models.OwnerBank

    def get_context_data(self, **kwargs):
        context = super(OwnerBankDelete, self).get_context_data(**kwargs)
        context["title"] = "DeleteBankAccount"
        context["delete"] = True
        return context

    def get_success_url(self):
        messages.success(self.request, "Successfully deleted")
        return reverse("fak_owner:bank_list")


# OWner views
