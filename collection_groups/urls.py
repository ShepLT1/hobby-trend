from django.urls import path
from . import views


urlpatterns = [
    path("", views.CollectionsView.as_view()),
    path("<uuid:collection_id>", views.CollectionView.as_view()),
    path(
        "items/<uuid:item_id>",
        views.CollectionItemView.as_view(),
    ),
]
