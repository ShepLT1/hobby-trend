import requests
import urllib
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
from data_cottage.settings import env
import json


class TCGPlayer:
    def __init__(self):
        self.base_url = env("SCRYFALL_BASE_URL")
        self.source_name = "TCGPlayer"

    def get_item_by_id(self, tcgplayer_card_id):
        response = dict(
            requests.get(
                self.base_url + "/cards/tcgplayer/" + str(tcgplayer_card_id)
            ).json()
        )
        return response

    def initialize_item(self, item, marketplace_item):
        params = urllib.parse.urlencode({"exact": item.name})
        response = dict(requests.get(self.base_url + "/cards/named?" + params).json())
        if response.status == 404:
            raise Exception(response.details)
        else:
            marketplace_item.data.id = response.tcgplayer_id
            self.create_listing(item, marketplace_item)
            marketplace_item.save()
            return response

    def create_listing(self, item, marketplace, marketplace_item):
        new_listing = Listing.objects.create(
            {
                "item": item,
                "source": marketplace,
                "price": marketplace_item.prices.usd,
                "link": marketplace_item.purchase_uris.tcgplayer,
            }
        )
        return new_listing
