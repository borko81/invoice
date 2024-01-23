from typing import Any
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from . import forms

from .helpers.bulstat_parse import GetDataFromBulstat


class ViewAllClients(LoginRequiredMixin, ListView):
    model = models.Client
    template_name = "fak_owner/clients.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Clients"
        return context

    def get_queryset(self):
        search_field = self.request.GET.get("search_field")
        queryset = models.Client.objects.all()
        if search_field and search_field == "active":
            queryset = models.Client.filtered_objects.only_active()
        elif search_field and search_field == "unactive":
            queryset = models.Client.filtered_objects.only_unactive()
        return queryset


class ClientNew(LoginRequiredMixin, CreateView):
    model = models.Client
    template_name = "fak_owner/clients.html"
    form_class = forms.ClientForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "NewClient"
        context["create"] = True
        return context

    def get_success_url(self) -> str:
        messages.success(self.request, "New client was successfully created")
        return reverse("fak_owner:clients")


class ClientEdit(LoginRequiredMixin, UpdateView):
    model = models.Client
    template_name = "fak_owner/clients.html"
    form_class = forms.ClientForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "EditClient"
        context["edit"] = True
        return context

    def get_success_url(self) -> str:
        messages.success(self.request, "Edit data was successfully")
        return reverse("fak_owner:clients")


class ClientDelete(LoginRequiredMixin, DeleteView):
    model = models.Client
    template_name = "fak_owner/clients.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "DeleteClient"
        context["delete"] = True
        return context

    def get_success_url(self) -> str:
        messages.success(self.request, "Record was successfully deleted")
        return reverse("fak_owner:clients")


def parse_bulstat(request, bulstat):
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

    if is_ajax:
        if request.method == "GET":
            data = GetDataFromBulstat(bulstat).parse_data()
            return JsonResponse(data)
        return JsonResponse({"status": "Invalid request"}, status=400)
    else:
        return JsonResponse({"status": "Invalid request"}, status=400)
