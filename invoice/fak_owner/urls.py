from django.urls import path
from . import views as app_views
from . import views_owner as owner_views
from . import views_clients as clients_views
from . import views_fak as fak_views

app_name = "fak_owner"
urlpatterns = [
    # OwnerBank urls'
    path("bank/", app_views.OwnerBankListView.as_view(), name="bank_list"),
    path("bank_new/", app_views.OwnerBanNew.as_view(), name="bank_new"),
    path("bank_edit/<int:pk>/", app_views.OwnerBankEdit.as_view(), name="bank_edit"),
    path(
        "bank_delete/<int:pk>/", app_views.OwnerBankDelete.as_view(), name="bank_delete"
    ),
    # Owner url's
    path("owner/", owner_views.OwnerView.as_view(), name="owner"),
    path("owner_new/", owner_views.OwnerNew.as_view(), name="owner_new"),
    path("owner_edit/<int:pk>/", owner_views.OwnerEdit.as_view(), name="owner_edit"),
    path(
        "owner_delete/<int:pk>/", owner_views.OwnerDelete.as_view(), name="owner_delete"
    ),
    # Clients url's
    path("clients/", clients_views.ViewAllClients.as_view(), name="clients"),
    path("client_new/", clients_views.ClientNew.as_view(), name="client_new"),
    path(
        "client_edit/<int:pk>/", clients_views.ClientEdit.as_view(), name="client_edit"
    ),
    path(
        "client_delete/<int:pk>/",
        clients_views.ClientDelete.as_view(),
        name="client_delete",
    ),
    path(
        "parse_data_from_web/<str:bulstat>/",
        clients_views.parse_bulstat,
        name="bulstat_parse",
    ),
    # Fak url's
    path("new_invoice/", fak_views.new_invoice, name="new_invoice"),
    path("invoices/", fak_views.invoices, name="invoices"),
]
