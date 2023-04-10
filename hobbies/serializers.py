from rest_framework import serializers
from .models import Hobby, ListingSource, Item, Listing, Media, Format, Variation, Set


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = (
            "id",
            "name",
            "type",
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


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = (
            "id",
            "name",
            "hobby",
            "created_at",
            "updated_at",
            "last_updated_by",
        )


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = (
            "id",
            "name",
            "item_count",
            "players",
            "estimated_time",
            "created_at",
            "updated_at",
            "last_updated_by",
        )


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = (
            "id",
            "name",
            "hobby",
            "format",
            "release_date",
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
            "sets",
            "variations",
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
