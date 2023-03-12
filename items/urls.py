from django.urls import path
from . import views


urlpatterns = [
    path("", views.ItemsView.as_view()),
    path("<uuid:item_id>", views.ItemView.as_view()),
]
