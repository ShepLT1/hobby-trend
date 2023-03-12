from django.db import models
from shared.models import BaseModel
from django.utils.translation import gettext_lazy as _


class ListingSource(BaseModel):
    name = models.CharField(null=False, max_length=64, default=None)

    def __str__(self) -> str:
        return self.name


class Hobby(BaseModel):
    class Meta:
        verbose_name_plural = "Hobbies"

    name = models.CharField(null=False, max_length=64, default=None)

    listing_sources = models.ManyToManyField(ListingSource)

    def __str__(self) -> str:
        return self.name


class UniversalCode(BaseModel):
    class typeChoices(models.TextChoices):
        SETNUM = "SN", _("Set Number")
        ISBN = "IS", _("ISBN")

    type = models.CharField(
        max_length=32, null=False, blank=False, choices=typeChoices.choices
    )

    value = models.CharField(max_length=32, unique=True, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class Price(BaseModel):
    date = models.DateField(null=False, blank=False)

    amount = models.DecimalField(max_digits=17, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class Media(BaseModel):
    title = models.CharField(null=False, max_length=64, default=None)

    src = models.URLField(default="https://google.com", max_length=512)

    alt = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Retailer(BaseModel):
    source = models.ForeignKey(
        ListingSource, on_delete=models.CASCADE, related_name="source"
    )

    price = models.ManyToManyField(Price)

    media = models.ManyToManyField(Media)

    def __str__(self) -> str:
        return self.name


class Item(BaseModel):
    name = models.CharField(null=False, max_length=256, default=None)

    hobby = models.ForeignKey(
        Hobby, on_delete=models.CASCADE, related_name="item_hobby"
    )

    release_date = models.DateField(null=True, blank=True)

    retailers = models.ManyToManyField(Retailer)

    universal_codes = models.ManyToManyField(UniversalCode)

    def __str__(self) -> str:
        return self.name
