from io import BytesIO

from PIL import Image
from celery.app import shared_task
from django.core.files import File


@shared_task()
def resize_image(instance_id):
    from users.models import Blog
    instance = Blog.objects.get(id=instance_id)
    original_image = Image.open(instance.image)

    dimensions = [("thumbnail", (100, 100)), ("medium", (300, 300)), ("large", (600, 600))]

    for dimension in dimensions:
        resized_image = original_image.resize(dimension[1], Image.ANTIALIAS)

        # Saving the images
        temp = BytesIO()
        resized_image.save(temp, format='JPEG')
        temp.seek(0)
        setattr(instance, dimension[0] + '_image', File(temp, instance.image.name))
    instance.save()
