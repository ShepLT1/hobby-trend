from django.contrib import admin

from .models import (
    Hobby,
    ListingSource,
    UniversalCode,
    Price,
    Media,
    Retailer,
    Item,
)
from shared.admin import BaseAdmin

admin.site.register(Hobby, BaseAdmin)
admin.site.register(ListingSource, BaseAdmin)
admin.site.register(UniversalCode, BaseAdmin)
admin.site.register(Price, BaseAdmin)
admin.site.register(Media, BaseAdmin)
admin.site.register(Retailer, BaseAdmin)
admin.site.register(Item, BaseAdmin)
