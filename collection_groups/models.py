from django.db import models
from shared.models import BaseModel
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from items.models import Item, Hobby


class Collection(BaseModel):
    name = models.CharField(null=False, max_length=64, default=None)

    hobby = models.ForeignKey(
        Hobby, on_delete=models.CASCADE, related_name="collection_hobby", default=1
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", default=1
    )

    def __str__(self) -> str:
        return self.name


class Condition(BaseModel):
    class ConditionChoices(models.TextChoices):
        NEW = "NE", _("New")
        MINT = "MT", _("Mint")
        LIKENEW = "LN", _("Used (Like new)")
        NEARMINT = "NM", _("Used (Near mint)")
        EXCELLENT = "EX", _("Used (Excellent)")
        VERYGOOD = "VG", _("Used (Very good)")
        GOOD = "GD", _("Used (Good)")
        LIGHTPLAYED = "LP", _("Used (Lightly played)")
        PLAYED = "PL", _("Used (Played)")
        POOR = "PR", _("Used (Poor)")
        OPEN = "OB", _("Used (Open box)")

    name = models.CharField(
        max_length=2, null=False, blank=False, choices=ConditionChoices.choices
    )

    hobby = models.ManyToManyField(Hobby, related_name="condition_hobby", default=1)

    def __str__(self) -> str:
        return self.name


class CollectionItem(BaseModel):

    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="item", default=1
    )

    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name="collection", default=1
    )

    condition = models.ManyToManyField(Condition, related_name="condition", default=1)

    serial_number = models.CharField(max_length=32, blank=True)

    def __str__(self) -> str:
        return self.item.name
