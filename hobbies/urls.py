from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.HobbiesView.as_view({"get": "list", "post": "create"})),
    path("<uuid:hobby_id>", views.HobbyView.as_view()),
    path(
        "<uuid:hobby_id>/items",
        views.ItemsView.as_view({"get": "list", "post": "create"}),
    ),
    path("items/<uuid:item_id>", views.ItemView.as_view()),
    path(
        "items/<uuid:item_id>/listings",
        views.ListingsView.as_view({"get": "list", "post": "create"}),
    ),
]
