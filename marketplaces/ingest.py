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
from marketplaces.marketplace_service_class.client import Marketplace


def ingest_listings_by_hobby(hobby):
    marketplace_client_dict = {"ebay": Ebay(), "tcgplayer": TCGPlayer()}
    items = Item.objects.filter(hobby_id=getattr(hobby, "id"))
    marketplaces = Marketplace.objects.filter(hobby=hobby)
    marketplace_clients = []
    for marketplace in marketplaces:
        marketplace_clients.append(marketplace_client_dict[marketplace.name.lower()])
    for item in items:
        for marketplace_client in marketplace_clients:
            marketplace = Marketplace(marketplace_client)
            marketplace.ingest_listing(item)
