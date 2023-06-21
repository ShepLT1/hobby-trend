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
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError


class Ebay:
    def __init__(self):
        self.source_name = "Ebay"
        self.find_api = Finding(
            domain="svcs.sandbox.ebay.com", appid=env("EBAY_APP_ID"), config_file=None
        )

    def get_item(self, marketplace_item):
        try:
            # CD (card game category for ebay) = 183454
            category_id = marketplace_item.marketplace.data["category_ids"][
                marketplace_item.item.hobby.type
            ]
            response = self.find_api.execute(
                "findItemsByKeywords",
                {
                    "keywords": marketplace_item.item.name,
                    "categoryId": category_id,
                    "sortOrder": "PricePlusShippingLowest",
                },
            )
            lowest_price_listing = self.choose_listing(response, marketplace_item.item)
            return lowest_price_listing
        except ConnectionError as e:
            print(e.response.dict())
            raise Exception(e)

    def choose_listing(self, listings, item):
        for response_item in listings.dict()["searchResult"]["item"]:
            if response_item["title"].lower() == item.name.lower():
                return response_item
        return None

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
            try:
                category_id = marketplace_item.marketplace.data["category_ids"][
                    marketplace_item.item.hobby.type
                ]
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
            lowest_price_item = self.choose_listing(response, item)
            if lowest_price_item is not None:
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
            item=item,
            source=marketplace,
            price=marketplace_item_listing["sellingStatus"]["currentPrice"]["value"],
            link=marketplace_item_listing["viewItemURL"],
        )
        return new_listing
