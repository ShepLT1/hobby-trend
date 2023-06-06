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
    ItemExternalSource,
)
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from data_cottage.settings import env
import json


class API:
    def __init__(self, client):
        self.client = client

    def get_item(self, item):
        item_external_source = ItemExternalSource.objects.get(
            item=item,
            listing_source=Marketplace.objects.get(name=self.client.source_name),
        )
        if item_external_source.data["id"] == None:
            response = self.client.initialize_item(item)
            pass
        else:
            response = self.client.get_item_by_id(item_external_source.data["id"])
        return response
