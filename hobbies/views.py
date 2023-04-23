from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from rest_framework import status, viewsets, pagination
from rest_framework.response import Response
from rest_framework.views import APIView
import uuid
from .serializers import (
    HobbySerializer,
    ListingSourceSerializer,
    ItemSerializer,
    ListingSerializer,
    MediaSerializer,
    SetSerializer,
)
from .models import Hobby, ListingSource, Item, Listing, Media, Set

# Create your views here.
class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 200


class HobbiesView(viewsets.ModelViewSet):
    serializer_class = HobbySerializer
    queryset = Hobby.objects.all()

    def perform_create(self, serializer):
        serializer.save(last_updated_by=self.request.user)


class HobbyView(APIView):
    def get(self, request, hobby_id: uuid, format=None):
        hobby = get_object_or_404(Hobby, id=hobby_id)
        serializer = HobbySerializer(hobby)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListingSourcesView(viewsets.ModelViewSet):
    serializer_class = ListingSourceSerializer
    queryset = ListingSource.objects.all()


class ItemsView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Item.objects.filter(hobby__id=self.kwargs["hobby_id"])
        return queryset

    def perform_create(self, serializer):
        serializer.save(last_updated_by=self.request.user)


class ItemView(APIView):
    def get(self, request, item_id: uuid, format=None):
        item = get_object_or_404(Item, id=item_id)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, item_id: uuid, format=None):
        item = get_object_or_404(Item, id=item_id)
        serializer = ItemSerializer(instance=item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SetsView(viewsets.ModelViewSet):
    serializer_class = SetSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Set.objects.filter(hobby__id=self.kwargs["hobby_id"])
        return queryset

    def perform_create(self, serializer):
        serializer.save(last_updated_by=self.request.user)


class SetView(APIView):
    def get(self, request, set_id: uuid, format=None):
        set = get_object_or_404(Set, id=set_id)
        serializer = SetSerializer(set)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, set_id: uuid, format=None):
        set = get_object_or_404(Set, id=set_id)
        serializer = SetSerializer(instance=set, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListingsView(viewsets.ModelViewSet):
    serializer_class = ListingSerializer

    def get_queryset(self):
        range = self.request.query_params.get("range")
        if range is None:
            range = 30
        else:
            range = int(range)
        queryset = Listing.objects.filter(
            item__id=self.kwargs["item_id"],
            created_at__gte=datetime.now() - timedelta(days=range),
        ).order_by("-created_at")
        return queryset

    def perform_create(self, serializer):
        serializer.save(last_updated_by=self.request.user)


class MediaView(viewsets.ModelViewSet):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()


class SingleMediaView(APIView):
    def put(self, request, media_id: uuid, format=None):
        media = get_object_or_404(Media, id=media_id)
        serializer = MediaSerializer(instance=media, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
