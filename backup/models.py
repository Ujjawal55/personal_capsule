from django.db import models
import uuid

# Create your models here.


class Bookmark(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.title)
