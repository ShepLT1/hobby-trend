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


class Scryfall:
    def __init__(self):
        self.base_url = env("SCRYFALL_BASE_URL")
        self.source_name = "Scryfall"

    def get_item_by_id(self, scryfall_card_id):
        response = dict(
            requests.get(self.base_url + "/cards/" + str(scryfall_card_id)).json()
        )
        return response

    def initialize_item(self, item):
        # TODO: get list of cards from scryfall that match name, determine which variation is correct, save card id (and other relevant info) in db, & return payload of correct variation
        pass
