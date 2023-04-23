from rest_framework import serializers
from .models import Collection, CollectionItem, Condition


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = (
            "id",
            "name",
            "hobby",
            "user",
            "type",
            "created_at",
            "updated_at",
            "last_updated_by",
        )


class CollectionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionItem
        fields = (
            "id",
            "item",
            "collection",
            "condition",
            "serial_number",
            "created_at",
            "updated_at",
            "last_updated_by",
        )


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = (
            "id",
            "name",
            "hobby",
            "created_at",
            "updated_at",
            "last_updated_by",
        )
