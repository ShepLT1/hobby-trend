from django.contrib import admin

from .models import (
    Hobby,
    ListingSource,
    Media,
    Listing,
    Item,
)
from shared.admin import BaseAdmin

admin.site.register(Hobby, BaseAdmin)
admin.site.register(ListingSource, BaseAdmin)
admin.site.register(Media, BaseAdmin)
admin.site.register(Listing, BaseAdmin)
admin.site.register(Item, BaseAdmin)
