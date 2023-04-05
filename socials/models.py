import uuid as uuid

from allauth.socialaccount.models import SocialAccount
from django.db import models
from django_extensions.db.models import TimeStampedModel


class TrafficData(TimeStampedModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    account = models.ForeignKey(SocialAccount, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    followers = models.IntegerField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    shares = models.IntegerField(blank=True, null=True)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}/{2}'.format(instance.account.user.username, instance.account.platform, filename)


class SocialPost(TimeStampedModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    account = models.ForeignKey(SocialAccount, on_delete=models.CASCADE, blank=True, null=True)
    date_published = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    # The file field can be used to store video or images
    file = models.FileField(upload_to=user_directory_path)
    likes = models.IntegerField(blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    shares = models.IntegerField(blank=True, null=True)
    published = models.BooleanField(default=False)
    header = models.JSONField(default=dict)
    data = models.JSONField(default=dict)
    response = models.JSONField(default=dict)


class SocialComments(TimeStampedModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    account = models.ForeignKey(SocialAccount, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(SocialPost, on_delete=models.CASCADE, blank=True, null=True)
    date_published = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    # The file field can be used to store video or images
    file = models.FileField(upload_to=user_directory_path)
    likes = models.IntegerField(blank=True, null=True)
    shares = models.IntegerField(blank=True, null=True)
    published = models.BooleanField(default=False)
    header = models.JSONField(default=dict)
    data = models.JSONField(default=dict)
    response = models.JSONField(default=dict)


class SocialCampaign(TimeStampedModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    account = models.ForeignKey(SocialAccount, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(SocialPost, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    spend = models.DecimalField(max_digits=12, decimal_places=3, default=None, blank=True, null=True)


# you can create a campaign, in that it could be external or internal
# other users in the system would see the campaign if its internal,
# users can the repost our post as their post on their social media
# the system then reward them based on engagements (views, like, reactions)


class SocialCampaignMetric(TimeStampedModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    campaign = models.ForeignKey(SocialCampaign, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    impressions = models.IntegerField(blank=True, null=True)
    clicks = models.IntegerField(blank=True, null=True)
    conversions = models.IntegerField(blank=True, null=True)


# this is the aggregated impression, clicks, conversions on a campaign

class SocialInfluencer(TimeStampedModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    account = models.ForeignKey(SocialAccount, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    followers = models.IntegerField(blank=True, null=True)
    engagement = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

# reach and influencer status, by reaching a certain numbers of followers and engagements
