from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    """
    A base model which includes created_at, updated_at, last_updated_by, and pk as uuid.
    """

    class Meta:
        abstract = True
        ordering = ["-updated_at"]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    id = models.UUIDField(primary_key=True, default=uuid4)
