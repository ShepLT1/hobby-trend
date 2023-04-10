from django.contrib import admin

from .models import Collection, CollectionItem, Condition
from shared.admin import BaseAdmin


admin.site.register(Collection, BaseAdmin)
admin.site.register(CollectionItem, BaseAdmin)
admin.site.register(Condition, BaseAdmin)
