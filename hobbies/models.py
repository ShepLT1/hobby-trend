from django.db import models
from shared.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Hobby(BaseModel):
    class Meta:
        verbose_name_plural = "Hobbies"

    class HobbyTypeChoices(models.TextChoices):
        CARD = "CD", _("Collectible card")
        GAME = "GM", _("Game")
        BASIC = "BC", _("Basic collection")

    class CodeTypeChoices(models.TextChoices):
        SETNUM = "SN", _("Set Number")
        ISBN = "IS", _("ISBN")
        CARDNUM = "CN", _("Card Number")

    name = models.CharField(max_length=64, default=None)

    type = models.CharField(
        max_length=2,
        null=False,
        blank=False,
        choices=HobbyTypeChoices.choices,
        default="BC",
    )

    universal_code_type = models.CharField(
        max_length=2,
        null=False,
        blank=False,
        choices=CodeTypeChoices.choices,
        default=None,
    )

    def __str__(self) -> str:
        return self.name


class ListingSource(BaseModel):
    name = models.CharField(max_length=64, default=None)

    hobby = models.ManyToManyField(Hobby, related_name="listing_hobby", default=[1])

    def __str__(self) -> str:
        return self.name


class Variation(BaseModel):
    name = models.CharField(unique=True, max_length=256, default=None)

    hobby = models.ForeignKey(
        Hobby, on_delete=models.CASCADE, related_name="variation_hobby", default=1
    )

    def __str__(self) -> str:
        return f"{self.name} ({self.hobby.name})"


class Format(BaseModel):
    name = models.CharField(unique=True, max_length=256, default=None)

    hobby = models.ForeignKey(
        Hobby, on_delete=models.CASCADE, related_name="format_hobby", default=1
    )

    item_count = models.IntegerField(default=1)

    players_min = models.IntegerField(verbose_name="Maximum # of Players", default=1)

    players_max = models.IntegerField(verbose_name="Minimum # of Players", default=1)

    # in minutes
    average_time = models.IntegerField(
        verbose_name="Average Game Time (minutes)", default=20
    )

    def __str__(self) -> str:
        return self.name


class Set(BaseModel):
    name = models.CharField(max_length=256, default=None)

    hobby = models.ForeignKey(
        Hobby, on_delete=models.CASCADE, related_name="set_hobby", default=1
    )

    format = models.ForeignKey(
        Format, on_delete=models.CASCADE, related_name="set_format", default=1
    )

    release_date = models.DateField(null=True)

    def __str__(self) -> str:
        return self.name


class Item(BaseModel):
    name = models.CharField(max_length=256, default=None)

    hobby = models.ForeignKey(
        Hobby, on_delete=models.CASCADE, related_name="item_hobby", default=1
    )

    sets = models.ManyToManyField(Set, blank=True, related_name="item_set", default=[1])

    variations = models.ManyToManyField(
        Variation, blank=True, related_name="item_variation", default=[1]
    )

    release_date = models.DateField(null=True)

    universal_code = models.CharField(unique=True, max_length=32, default=None)

    def __str__(self) -> str:
        return self.name


class Listing(BaseModel):

    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="listing_item", default=1
    )

    source = models.ForeignKey(
        ListingSource, on_delete=models.CASCADE, related_name="source", default=1
    )

    date = models.DateField()

    price = models.DecimalField(max_digits=17, decimal_places=2)

    link = models.URLField(default="https://google.com", max_length=512)

    def __str__(self) -> str:
        return f"{self.item.name} ({self.source} {self.date})"


class Media(BaseModel):
    class Meta:
        verbose_name_plural = "Media"

    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="media_item", default=1
    )

    title = models.CharField(max_length=64, default=None)

    src = models.URLField(default="https://google.com", max_length=512)

    alt = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
