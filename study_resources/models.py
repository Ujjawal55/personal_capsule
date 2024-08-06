from django.db import models

# Create your models here.


class Bookmark(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return str(self.title)
