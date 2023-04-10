from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.HobbiesView.as_view({"get": "list"})),
    path("items/", views.ItemsView.as_view({"get": "list"})),
    path("items/<uuid:item_id>", views.ItemView.as_view()),
]
