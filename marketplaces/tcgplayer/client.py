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


class Tcgplayer:
    def __init__(self):
        self.base_url = env("SCRYFALL_BASE_URL")

    def get_card(self, card):
        card_external_source = ItemExternalSource.objects.get(
            item=card, listing_source=Marketplace.objects.get(name="TCGplayer")
        )
        if card_external_source.data["id"] == None:
            return {}
        scryfall_card_id = card_external_source.data["id"]
        response = dict(
            requests.get(
                self.base_url + "/cards/tcgplayer" + str(scryfall_card_id)
            ).json()
        )
        return response
