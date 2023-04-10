from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.ItemsView.as_view({"get": "list"})),
    path("<uuid:item_id>", views.ItemView.as_view({"get": "list"})),
]
