from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("list/", views.list_View, name="list"),
    path("create/", views.create_View, name="create"),
    path("detail/<id>/", views.detail_View, name="detail"),
]
