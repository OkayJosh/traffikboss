import logging
import requests
import datetime

from celery import shared_task
from asgiref.sync import async_to_sync

# from socials.calls import get_social_media_data
from socials.models import SocialPost

LOG = logging.getLogger(__name__)


@shared_task()
def retrieve_social_posts():
    # Make API requests to retrieve social media data
    # data = get_social_media_data()
    data = None
    # Iterate over the retrieved data and create new SocialPost records
    for item in data:
        post = SocialPost(
            account=item['account'],
            post_id=item['id'],
            date_published=item['created_time'],
            content=item['message'],
            likes=item['likes']['summary']['total_count'],
            comments=item['comments']['summary']['total_count'],
            shares=item.get('shares', {}).get('count', 0),
        )
        post.save()


@shared_task()
def check_app_status(self):
    global app_offline_since
    try:
        response = requests.get('https://traffikboss.com/status')
        if response.status_code == 200:
            # app is online
            if app_offline_since is not None:
                # app was previously offline
                # send notification indicating the app is back online
                async_to_sync(self.send)('ONLINE')
            app_offline_since = None
        else:
            # app is offline
            app_offline_since = datetime.datetime.now()
            # send the output to the client over the WebSocket connection
            async_to_sync(self.send)(response.status_code)
    except Exception as e:
        # log the incident and send an alert
        LOG.exception('Error while checking app status: %s', e)
