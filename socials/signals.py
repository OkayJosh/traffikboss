from allauth.socialaccount.models import SocialToken
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=SocialToken)
def save_token(sender, instance, **kwargs):
    # Save the access_token in your database
    pass
