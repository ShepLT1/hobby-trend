from hobbies.models import (
    Hobby,
    Marketplace,
    Media,
    Listing,
    Item,
    Set,
    Format,
    Variation,
    MarketplaceItem,
)
from marketplaces.ebay.client import Ebay
from marketplaces.tcgplayer.client import TCGPlayer
from marketplaces.marketplace_service_class.client import MarketplaceWrapper
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


def ingest_listings_by_hobby(hobby):
    marketplace_client_dict = {"ebay": Ebay(), "tcgplayer": TCGPlayer()}
    items = Item.objects.filter(hobby__id=getattr(hobby, "id"))
    marketplaces = Marketplace.objects.filter(hobby__id=getattr(hobby, "id"))
    marketplace_clients = []
    for marketplace in marketplaces:
        marketplace_clients.append(marketplace_client_dict[marketplace.name.lower()])
    for item in items:
        for marketplace_client in marketplace_clients:
            marketplace = MarketplaceWrapper(marketplace_client)
            marketplace.ingest_listing(item)
