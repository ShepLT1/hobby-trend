from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.CollectionsView.as_view({"get": "list", "post": "create"})),
    path("<uuid:collection_id>", views.CollectionView.as_view()),
    path(
        "<uuid:collection_id>/items",
        views.CollectionItemsView.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "items/<uuid:collection_item_id>",
        views.CollectionItemView.as_view(),
    ),
]
