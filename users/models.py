import uuid as uuid

from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import AbstractUser

from users.tasks import resize_image


class User(TimeStampedModel, AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='user_parent')
    account_type = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    fcmb_token = models.CharField(max_length=255, blank=True, null=True)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class ResetToken(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reset_token')
    token = models.CharField(max_length=255, blank=True, null=True)


class Blog(TimeStampedModel):
    name = models.CharField(max_length=256, blank=True, null=True)
    image = models.FileField(blank=True, null=True)
    thumbnail_image = models.FileField(blank=True, null=True)
    medium_image = models.FileField(blank=True, null=True)
    large_image = models.FileField(blank=True, null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Blog"
        get_latest_by = ['created', 'updated']
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)
        resize_image.apply_async(args=(self.id,))

    @property
    def comment_count(self):
        return self.blog_comment.exists()

    @property
    def preview(self):
        return self.slice_sentence(self.content, 20)

    @staticmethod
    def slice_sentence(sentence, n):
        words = sentence.split()
        if n <= len(words):
            return ' '.join(words[:n])
        return sentence


class BlogComment(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='user_blog_comment', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='comment_blog_parent', null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, related_name='blog_comment', null=True, blank=True)
    body = models.TextField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.blog.name


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.username, filename)


class Ticket(TimeStampedModel):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=None)
    subject = models.CharField(max_length=200, unique=True)
    issue = models.TextField()
    document = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    resolved = models.BooleanField(default=False, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        db_table = "Ticket"
        get_latest_by = ['created', 'updated']
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    def __str__(self) -> str:
        return self.subject

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject)
        super(Ticket, self).save(*args, **kwargs)

    @property
    def documenturl(self):
        try:
            url = self.document.url
        except:
            url = False
        return url

    @property
    def comment_count(self):
        return self.comment.exists()


class TicketComment(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='user_ticket_comment', null=True, blank=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, related_name='comment', null=True, blank=True)
    body = models.TextField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'comment from {self.user} to {self.ticket.subject} ticket'


class Plan(TimeStampedModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    monthly_price = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    benefits = models.ForeignKey(to='Benefits', related_name='plan_benefits', on_delete=models.SET_NULL,
                                 blank=True, null=True)


class Benefits(TimeStampedModel):
    details = models.CharField(max_length=255, blank=True, null=True)


class SystemPlanDiscount(TimeStampedModel):
    yearly_discount = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=3)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SystemPlanDiscount, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class Testimonials(TimeStampedModel):
    ratings = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=3)
    testimonials = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='users_testimonials', on_delete=models.SET_NULL, blank=True, null=True)


class FAQ(TimeStampedModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()


class Newsletter(TimeStampedModel):
    email = models.EmailField(blank=True, null=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    device = models.CharField(max_length=255, blank=True, null=True)
    device_model = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)


class SystemContact(TimeStampedModel):
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SystemContact, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class ContactUs(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='user_contact', null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
