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
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

# import xmltodict
# import json


class Ebay:
    def __init__(self):
        self.source_name = "Ebay"
        self.find_api = Finding(appid=env("EBAY_APP_ID"), config_file=None)

    def get_items_by_id(self, item_ebay_id):
        try:
            response = self.find_api.execute(
                "findItemsByProduct",
                {"productId": {"type": "ReferenceID", "value": item_ebay_id}},
            )
            return response.dict()
        except ConnectionError as e:
            print(e.response.dict())
            raise Exception(e)

    def initialize_item(self, item, marketplace_item):
        universal_code_type = item.hobby.universal_code_type
        if universal_code_type == "UPC" or universal_code_type == "ISBN":
            try:
                response = self.find_api.execute(
                    "findItemsByProduct",
                    {
                        "productId": {
                            "type": universal_code_type,
                            "value": item.universal_code,
                        }
                    },
                )
            except ConnectionError as e:
                print(e.response.dict())
                raise Exception(e)
        else:
            # CD (card game category for ebay) = 183454
            category_id = marketplace_item.marketplace.data.category_ids[
                item.hobby.type
            ]
            try:
                response = self.find_api.execute(
                    "findItemsByKeywords",
                    {
                        "keywords": item.name,
                        "categoryId": category_id,
                        "sortOrder": "PricePlusShippingLowest",
                    },
                )
            except ConnectionError as e:
                print(e.response.dict())
                raise Exception(e)
            lowest_price_item = None
            for item in response.dict()["searchResult"]:
                if item["title"].lower() == item.name.lower():
                    lowest_price_item = item
                    break
            if lowest_price_item is not None:
                marketplace_item.data.id = lowest_price_item.productId
                self.ingest_listing(
                    item, marketplace_item.marketplace, lowest_price_item
                )
                marketplace_item.save()
                return lowest_price_item
            else:
                raise Exception(
                    f"No matching item found on Ebay for item name {item.name}"
                )

    def ingest_listing(self, item, marketplace, marketplace_item_listing):
        new_listing = Listing.objects.create(
            {
                "item": item,
                "source": marketplace,
                "price": marketplace_item_listing.listinginfo.buyItNowPrice,
                "link": marketplace_item_listing.viewItemURL,
            }
        )
        return new_listing
