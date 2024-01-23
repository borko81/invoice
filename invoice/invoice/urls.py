from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout/", views.logout_view, name="custom_logout"),
    path("", views.check_base, name="base_template"),
    path("", include("fak_owner.urls")),
    path("config/", include("hotel_config.urls")),
    path("nast/", include("nast_config.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
