from django.contrib import admin

from .models import (
    Hobby,
    Marketplace,
    Media,
    Listing,
    Item,
    Set,
    Format,
    Variation,
    ItemExternalSource,
)
from shared.admin import BaseAdmin

admin.site.register(Hobby, BaseAdmin)
admin.site.register(Marketplace, BaseAdmin)
admin.site.register(Media, BaseAdmin)
admin.site.register(Listing, BaseAdmin)
admin.site.register(Item, BaseAdmin)
admin.site.register(Set, BaseAdmin)
admin.site.register(Format, BaseAdmin)
admin.site.register(Variation, BaseAdmin)
admin.site.register(ItemExternalSource, BaseAdmin)
