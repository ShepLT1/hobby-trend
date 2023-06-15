import requests
from hobbies.models import (
    Hobby,
    Marketplace,
    Variation,
    Format,
    Set,
    Item,
    Listing,
    Media,
    MarketplaceItem,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from hobby_trend.settings import env
import json


class MarketplaceWrapper:
    def __init__(self, client):
        self.client = client

    def get_item(self, item):
        marketplace_item = MarketplaceItem.objects.get(
            item=item,
            marketplace=Marketplace.objects.get(name=self.client.source_name),
        )
        if marketplace_item.data["id"] == None:
            response = self.client.initialize_item(item, marketplace_item)
        else:
            response = self.client.get_item_by_id(marketplace_item.data["id"])
        return response

    def ingest_listing(self, item):
        marketplace_item = self.get_item(item)
        marketplace = Marketplace.objects.get(name=self.client.source_name)
        response = self.client.ingest_listing(item, marketplace, marketplace_item)
        return response
