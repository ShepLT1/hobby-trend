from django.db import models
from shared.models import BaseModel
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from items.models import Item, Hobby


class Collection(BaseModel):
    name = models.CharField(null=False, max_length=64, default=None)

    hobby = models.ForeignKey(
        Hobby, on_delete=models.CASCADE, related_name="collection_hobby"
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    def __str__(self) -> str:
        return self.name


class CollectionItem(BaseModel):
    class ConditionChoices(models.TextChoices):
        NEW = "NE", _("New")
        LIKE = "LN", _("Used (Like new)")
        GOOD = "GD", _("Used (Good)")
        POOR = "PR", _("Used (Poor)")
        OPEN = "OB", _("Used (Open box)")

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item")

    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name="collection"
    )

    condition = models.CharField(
        max_length=32, null=False, blank=False, choices=ConditionChoices.choices
    )

    serial_number = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name
