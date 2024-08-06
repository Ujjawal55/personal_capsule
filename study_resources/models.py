from os import walk
from django.db import models

# Create your models here.


class ResourcesList(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return str(self.name)
