from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
import uuid
from .serializers import (
    HobbySerializer,
    ListingSourceSerializer,
    ItemSerializer,
    ListingSerializer,
    MediaSerializer,
)
from .models import Hobby, ListingSource, Item, Listing, Media

# Create your views here.


class HobbiesView(viewsets.ModelViewSet):
    serializer_class = HobbySerializer
    queryset = Hobby.objects.all()


class ListingSourcesView(viewsets.ModelViewSet):
    serializer_class = ListingSourceSerializer
    queryset = ListingSource.objects.all()


class ItemsView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


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


class ListingsView(viewsets.ModelViewSet):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()


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
