from django.db import models
import uuid
# Create your models here.
# NOTE: remove the blank and null property from the scheme.
# NOTE: how to upload the multiple images.


class Notes(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    body = models.TextField(blank=True)
    images = models.ImageField(upload_to="notes/images/", null=True, blank=True)
    is_viewd = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.title)
