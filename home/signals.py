from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from home.models import Profile

# TODO: have to enable the name variable after some time


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            name=user.first_name,
            email=user.email,
            username=user.username,
        )


def updateProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.first_name = profile.name
        user.email = profile.email
        user.username = profile.username


def deleteProfile(sender, instance, **kwargs):
    user = instance.user

    user.delete()


post_save.connect(receiver=createProfile, sender=User)
post_save.connect(receiver=updateProfile, sender=Profile)
post_delete.connect(receiver=deleteProfile, sender=Profile)
