from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmarks")
    title = models.CharField(max_length=255)
    url = models.URLField()
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.title)


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=False)
    url = models.URLField()
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.title)
