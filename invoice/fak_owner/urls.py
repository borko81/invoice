from django.urls import path
from . import views as app_views

app_name = "fak_owner"
urlpatterns = [
    path("bank/", app_views.OwnerBankListView.as_view(), name="bank_list"),
    path("bank_new/", app_views.OwnerBanNew.as_view(), name="bank_new"),
    path("bank_edit/<int:pk>/", app_views.OwnerBankEdit.as_view(), name="bank_edit"),
    path(
        "bank_delete/<int:pk>/", app_views.OwnerBankDelete.as_view(), name="bank_delete"
    ),
]
