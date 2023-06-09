from rest_framework import serializers
from .models import Hobby, Marketplace, Item, Listing, Media, Format, Variation, Set


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


class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketplace
        fields = (
            "id",
            "name",
            "hobby",
            "data",
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


# TODO: When adding set, if set hobby.type is not BC, format field is required
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


# TODO: When adding item that is part of a set, validate that item release date is before or equal to set release date
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


class MarketplaceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = (
            "id",
            "marketplace",
            "item",
            "data",
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
            "price",
            "shipping",
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
