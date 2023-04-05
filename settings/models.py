from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel

from users.managers import DeviceManager

""""
MAX_GET_SIGNUP = "0"
MAX_GET_TRAIL = "20"
MAX_GET_BASIC = "1000"
MAX_GET_PREMIUM = "10000"
MAX_GET_DELETED = "0"

MAX_CURL_SIGNUP = "0"
MAX_CURL_TRAIL = "20"
MAX_CURL_BASIC = "1728"
MAX_CURL_PREMIUM = "17280"
MAX_CURL_DELETED = "0"

REFERRAL_EARNING = 10

SYSTEM_COMMISSION = 5
TAX = 1

MAX_LINK_TRAIL = 1000
MAX_LINK_BASIC = 2000
MAX_LINK_PREMIUM = 3000
MAX_LINK_DELETED = 0

# Burst time is 5sec making 17,280 possible burst in a day
BURST_TIME = 5

USER_TYPE = {
    "TR": "TRAIL",
    "BA": "BASIC",
    "PR": "PREMIUM",
    "DE": "DELETED"
}
ALLOWED_IP = {
    "TRAIL": 1,
    "BASIC": 5,
    "PREMIUM": 10,
    "DELETED": 0
}

"""


class Device(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='logged_devices')
    device_name = models.CharField(max_length=255, blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    token = models.ForeignKey('authtoken.Token', blank=True, null=True, on_delete=models.CASCADE, related_name='device_token')
    objects = DeviceManager()