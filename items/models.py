from django.db import models
from shared.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Hobby(BaseModel):
    class Meta:
        verbose_name_plural = "Hobbies"

    class CodeTypeChoices(models.TextChoices):
        SETNUM = "SN", _("Set Number")
        ISBN = "IS", _("ISBN")

    name = models.CharField(null=False, max_length=64, default=None)

    universal_code_type = models.CharField(
        max_length=32,
        null=False,
        blank=False,
        choices=CodeTypeChoices.choices,
        default=None,
    )

    def __str__(self) -> str:
        return self.name


class ListingSource(BaseModel):
    name = models.CharField(null=False, max_length=64, default=None)

    hobby = models.ManyToManyField(Hobby, related_name="listing_hobby", default=1)

    def __str__(self) -> str:
        return self.name


class Item(BaseModel):
    name = models.CharField(null=False, max_length=256, default=None)

    hobby = models.ForeignKey(
        Hobby, on_delete=models.CASCADE, related_name="item_hobby", default=1
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

    date = models.DateField(null=False, blank=False)

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

    title = models.CharField(null=False, max_length=64, default=None)

    src = models.URLField(default="https://google.com", max_length=512)

    alt = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
