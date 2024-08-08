from django.db import models
from django.contrib.auth.models import User
import uuid
import os
# Create your models here.
# NOTE: remove the blank and null property from the scheme.
# NOTE: how to upload the multiple images.


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=30, null=True, blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="notes/images/", null=True, blank=True)
    is_viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.title)

    @property
    def filename(self):
        return os.path.basename(self.image.name)
