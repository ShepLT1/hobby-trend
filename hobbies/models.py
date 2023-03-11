from django.db import models
from shared.models import BaseModel
from django.contrib.auth.models import User
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


class Collection(BaseModel):
    name = models.CharField(null=False, max_length=64, default=None)

    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class UniversalCode(BaseModel):
    class typeChoices(models.TextChoices):
        SETNUM = "SN", _("Set Number")
        ISBN = "IS", _("ISBN")

    type = models.CharField(
        max_lengt=32, null=False, blank=False, choices=typeChoices.choices
    )

    value = models.CharField(max_lengt=32, unique=True, null=False, blank=False)

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
    source = models.ForeignKey(ListingSource, on_delete=models.CASCADE)

    price = models.ManyToManyField(Price)

    media = models.ManyToManyField(Media)

    def __str__(self) -> str:
        return self.name


class Item(BaseModel):
    name = models.CharField(null=False, max_length=256, default=None)

    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)

    release_date = models.DateField(null=True, blank=True)

    retailers = models.ManyToManyField(Retailer)

    universal_codes = models.ManyToManyField(UniversalCode)

    def __str__(self) -> str:
        return self.name


class CollectionItem(BaseModel):
    class ConditionChoices(models.TextChoices):
        NEW = "NE", _("New")
        LIKE = "LN", _("Used (Like new)")
        GOOD = "GD", _("Used (Good)")
        POOR = "PR", _("Used (Poor)")
        OPEN = "OB", _("Used (Open box)")

    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    condition = models.CharField(
        max_lengt=32, null=False, blank=False, choices=ConditionChoices.choices
    )

    serial_number = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name
