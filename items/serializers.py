from rest_framework import serializers
from .models import Hobby, ListingSource, Item, Listing, Media


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = (
            "id",
            "name",
            "universal_code_type",
            "created_at",
            "updated_at",
            "last_updated_by",
        )


class ListingSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingSource
        fields = (
            "id",
            "name",
            "hobby",
            "created_at",
            "updated_at",
            "last_updated_by",
        )


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "id",
            "name",
            "hobby",
            "release_date",
            "universal_code",
            "created_at",
            "updated_at",
            "last_updated_by",
        )


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = (
            "id",
            "item",
            "source",
            "date",
            "price",
            "link",
            "created_at",
            "updated_at",
            "last_updated_by",
        )


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = (
            "id",
            "item",
            "title",
            "src",
            "alt",
            "created_at",
            "updated_at",
            "last_updated_by",
        )
