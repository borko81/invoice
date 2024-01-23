from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from . import forms


class OwnerView(LoginRequiredMixin, ListView):
    template_name = "fak_owner/owner.html"
    model = models.Owner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Owner"
        return context


class OwnerNew(LoginRequiredMixin, CreateView):
    template_name = "fak_owner/owner.html"
    model = models.Owner
    form_class = forms.OwnerForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "NewOwner"
        context["create"] = True
        return context

    def get_success_url(self):
        messages.success(self.request, "Успешен запис")
        return reverse("fak_owner:owner")


class OwnerEdit(LoginRequiredMixin, UpdateView):
    template_name = "fak_owner/owner.html"
    model = models.Owner
    form_class = forms.OwnerForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "EditOwner"
        context["edit"] = True
        return context

    def get_success_url(self):
        messages.success(self.request, "Успешна редакция")
        return reverse("fak_owner:owner")


class OwnerDelete(LoginRequiredMixin, DeleteView):
    template_name = "fak_owner/owner.html"
    model = models.Owner
    # success_url = reverse_lazy("fak_owner:owner")

    def get_context_data(self, **kwargs):
        context = super(OwnerDelete, self).get_context_data(**kwargs)
        context["title"] = "DeleteOwner"
        context["delete"] = True
        return context

    def get_success_url(self):
        messages.success(self.request, "Successfully deleted")
        return reverse("fak_owner:owner")
