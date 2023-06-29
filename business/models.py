"""
Business Table:
business_id
brand_id (Foreign Key referencing the Brand table)
name
industry
description
address
contact_number

"""
from django_extensions.db.models import TimeStampedModel
from django.db import models

from users.models import user_directory_path


class Business(TimeStampedModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_number = models.CharField(max_length=255, blank=True, null=True)


class BusinessUrl(TimeStampedModel):
    """
        url_id (Primary Key)
        brand_id (Foreign Key referencing the Brand table)
        original_url
    """
    business = models.ForeignKey('Business', on_delete=models.SET_NULL, blank=True,
                                 null=True, related_name='business_url')
    original_url = models.URLField(blank=True, null=True)
    shortened_url = models.URLField(blank=True, null=True)


class Character(TimeStampedModel):
    """
            Character Table:
            tone
            character_id (Primary Key)
            name
            age
            gender
            description
            role
            abilities
            image_url
            backstory
            personality_traits
            relationships
            character_arc

    """
    tone = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    ability = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=user_directory_path)
    backstory = models.CharField(max_length=255, blank=True, null=True)
    personality_traits = models.CharField(max_length=255, blank=True, null=True)
    relationships = models.CharField(max_length=255, blank=True, null=True)
    arc = models.CharField(max_length=255, blank=True, null=True)