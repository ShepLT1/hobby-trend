from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from rest_framework import status, viewsets, pagination
from rest_framework.response import Response
from rest_framework.views import APIView
import uuid
from .serializers import CollectionSerializer, CollectionItemSerializer
from .models import Collection, CollectionItem

# Create your views here.
class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 200


class CollectionsView(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Collection.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(last_updated_by=self.request.user)


class CollectionView(APIView):
    def get(self, request, collection_id: uuid, format=None):
        collection = get_object_or_404(Collection, id=collection_id)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, collection_id: uuid, format=None):
        collection = get_object_or_404(Collection, id=collection_id)
        serializer = CollectionSerializer(
            instance=collection, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectionItemsView(viewsets.ModelViewSet):
    serializer_class = CollectionItemSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = CollectionItem.objects.filter(
            collection__id=self.kwargs["collection_id"]
        )
        return queryset

    def perform_create(self, serializer):
        serializer.save(last_updated_by=self.request.user)


class CollectionItemView(APIView):
    def get(self, request, collection_item_id: uuid, format=None):
        collection_item = get_object_or_404(CollectionItem, id=collection_item_id)
        serializer = CollectionItemSerializer(collection_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, collection_item_id: uuid, format=None):
        collection_item = get_object_or_404(CollectionItem, id=collection_item_id)
        serializer = CollectionItemSerializer(
            instance=collection_item, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
