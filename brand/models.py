from django.db import models
from django_extensions.db.models import TimeStampedModel

from users.models import user_directory_path


class Brand(TimeStampedModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    business = models.ForeignKey('business.Business', on_delete=models.SET_NULL, blank=True,
                                 null=True, related_name='brand_business')
    logo = models.FileField(upload_to=user_directory_path)
    description = models.CharField(max_length=255, blank=True, null=True)

    website_url = models.URLField(blank=True, null=True)
    contact_number = models.CharField(max_length=255, blank=True, null=True)
    numbers_of_daily_post = models.IntegerField(blank=True, null=True)


class BrandMonitor(TimeStampedModel):
    """
        Brand Performance Table:
        performance_id (Primary Key)
        brand_id (Foreign Key referencing the Brand table)
        date
        followers
        engagement_rate
        Sentiment_score

    """
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, blank=True,
                              null=True, related_name='brand_monitor')
    followers = models.PositiveBigIntegerField(blank=True, null=True)
    engagement_rate = models.CharField(max_length=255, blank=True, null=True)
    sentiment_score = models.CharField(max_length=255, blank=True, null=True)


class BrandPostTemplate(TimeStampedModel):
    """
    This is the template the Brand wants his post in or fashioned against
        Post Template Table:
        brand_id (Foreign Key referencing the Brand table)
        date
        head
        body
        close
        character_id (Foreign Key referencing the Character table)
        topic_id (Foreign Key referencing the Post Topic table)

    """

    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, blank=True,
                              null=True, related_name='brand_post_template')
    head = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    tail = models.CharField(max_length=255, blank=True, null=True)
    character = models.ForeignKey('business.Character', on_delete=models.SET_NULL, blank=True,
                                  null=True, related_name='brand_character')
    topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, blank=True,
                              null=True, related_name='brand_topic')


class Topic(TimeStampedModel):
    """
        The topics are areas the brand wants to talk/post about::
        default would be created based on the brand onboarding
        Post Topic Table:
            topic_id (Primary Key)
            name
            description

    """
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, blank=True,
                              null=True, related_name='brand_topic')


class BrandPostTime(TimeStampedModel):
    """
        The time in which the brand want there post to go out to the connected social media
        post_time
    """
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, blank=True,
                              null=True, related_name='brand_post_time')
    post_time = models.TimeField(blank=True, null=True)


class BrandMention(TimeStampedModel):
    """
        This is the mention reference for the brand, found on social media
        BrandMention Table:
            content
            brand_id
            sentiment_score
    """
    content = models.TextField()
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, blank=True,
                              null=True, related_name='brand_mention')
    sentiment_score = models.CharField(max_length=255, blank=True, null=True)