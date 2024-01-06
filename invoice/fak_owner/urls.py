from django.urls import path
from . import views as app_views
from . import views_owner as owner_views

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
]
