from django.urls import path
from . import views

app_name = "hotel"
urlpatterns = [
    path("floors/", views.floors, name="floors"),
    path("new_floor/", views.new_floor, name="new_floor"),
    path("delete_floor/<int:id_>/", views.delete_floor, name="delete_floor"),
    path("edit_floor/<int:id_>/", views.edit_floor, name="edit_floor"),
    # beds
    path("beds/", views.beds, name="beds"),
    path("new_bed/", views.new_bed, name="new_bed"),
    path("delete_bed/<int:id_>/", views.delete_bed, name="delete_bed"),
    path("edit_bed/<int:id_>/", views.edit_bed, name="edit_bed"),
]
