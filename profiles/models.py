from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    name = models.CharField(max_length=254)
    surname = models.CharField(max_length=254)
    ## There's a plugin for this! phone_number = 
    address_1 = models.CharField(max_length=254)
    address_2 = models.CharField(max_length=254)
    address_3 = models.CharField(max_length=254)
    address_country = models.CharField(max_length=254)
    address_postcode = models.CharField(max_length=254)
    newsletter_update = models.BooleanField(default=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # Creates a profile on creation of User, to be customsed
    if created:
        Profile.objects.create(user=instance)