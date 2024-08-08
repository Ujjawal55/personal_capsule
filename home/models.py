from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=190, null=True, blank=True)
    username = models.CharField(max_length=20, null=True, blank=True)
    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="profile/",
        default="profile/default-profile.png",
    )
    social_github = models.CharField(max_length=40, null=True, blank=True)
    social_linkedin = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_search = models.CharField(max_length=50, null=True, blank=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.username)
