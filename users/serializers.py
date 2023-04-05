from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.reverse import reverse

from users.models import Plan, Benefits, SystemPlanDiscount, User, Testimonials, Blog, FAQ, Newsletter, SystemContact, \
    ContactUs

from geopy.geocoders import Nominatim
from user_agents import parse
from cache_memoize import cache_memoize
from password_strength import PasswordPolicy

from users.services import UserService


class BenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits
        fields = ('details',)


class PlanSerializer(serializers.ModelSerializer):
    plan_benefits = BenefitsSerializer(many=True, read_only=True)

    class Meta:
        model = Plan
        fields = ('name', 'monthly_price', 'plan_benefits')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['price_per_month'] = rep.pop('monthly_price')
        rep['price_per_year'] = rep['price_per_month'] * 12
        from users.models import SystemPlanDiscount
        system_plan_discount = SystemPlanDiscount.load()
        if system_plan_discount:
            rep['price_per_year'] = rep['price_per_year'] * 1 - system_plan_discount
        return rep


class SystemPlanDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemPlanDiscount
        fields = ('yearly_discount',)


class SystemContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemContact
        fields = ('phone_number', 'email')


class TestimonialUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'member',)

    def get_member(self, obj):
        if obj is None:
            return 'Early Member'
        return 'Verified TraffikBoss Member'


class TestimonialSerializer(serializers.ModelSerializer):
    user = TestimonialUserSerializer(read_only=True)
    percentage = serializers.SerializerMethodField()

    class Meta:
        model = Testimonials
        fields = ('ratings', 'testimonials', 'user', 'percentage')

    def get_percentage(self, obj):
        return obj.ratings * 100


class BlogSerializer(serializers.ModelSerializer):
    title_blog = serializers.SerializerMethodField()
    min_content_blog = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ('title_blog', 'min_content_blog')

    def build_url(self, slug):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('blog-list') + slug)

    def get_title_blog(self, obj):
        return {
            'image_url': obj.medium_image.url,
            'published_date': obj.created,
            'title': obj.name,
            'url': self.build_url(obj.slug)
        }

    def get_min_content_blog(self, obj):
        return {
            'image_url': obj.thumbnail_image.url,
            'published_date': obj.created,
            'title': obj.name,
            'min_content': obj.preview,
            'url': self.build_url(obj.slug)
        }


class FullBlogSerializer(serializers.ModelSerializer):
    title_blog = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ('title_blog',)

    def get_title_blog(self, obj):
        return {
            'image_url': obj.medium_image.url,
            'published_date': obj.created,
            'title': obj.name,
            'min_content': obj.preview
        }

    def get_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(reverse('blog-list') + obj.slug)


class DetailedBlogSerializer(serializers.ModelSerializer):
    content = serializers.CharField(source='content')
    large_image = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ('content', 'large_image',)

    def get_url(self, obj):
        request = self.context.get('request')
        large_image_url = obj.large_image.url
        return request.build_absolute_uri(large_image_url)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['get_title_blog'] = FullBlogSerializer(data=self.Meta.model.objects.all().order_by('-created')[:5]).data
        return rep


class FAQSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='name')
    answer = serializers.CharField(source='content')

    class Meta:
        model = FAQ
        fields = ('question', 'answer')


class NewsletterSerializer(serializers.ModelSerializer):
    ip_address = serializers.SerializerMethodField()
    device = serializers.SerializerMethodField()
    device_model = serializers.SerializerMethodField()
    version = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        model = Newsletter
        fields = ('email', 'ip_address', 'device', 'device_model', 'version', 'location')

    def get_ip_address(self, obj):
        return self.context['request'].META.get('REMOTE_ADDR')

    def get_device(self, obj):
        user_agent = self.context['request'].META.get('HTTP_USER_AGENT')
        device = parse(user_agent)
        return device.get_device()

    def get_device_model(self, obj):
        user_agent = self.context['request'].META.get('HTTP_USER_AGENT')
        device = parse(user_agent)
        return device.get_os()

    def get_version(self, obj):
        user_agent = self.context['request'].META.get('HTTP_USER_AGENT')
        device = parse(user_agent)
        print(device, 'device')
        if not device:
            return "Unknown"
        else:
            return str(device)

    # @cache_memoize(60 * 15)
    def get_location(self, obj):
        ip_address = self.context['request'].META.get('REMOTE_ADDR')
        if ip_address not in  ["127.0.0.1"]:
            user_agent = settings.PROJECT_APP_NAME + "/1.0"
            geolocator = Nominatim(user_agent=user_agent)
            location = geolocator.geocode(ip_address, timeout=4)
            if location:
                return location.address
            else:
                return ip_address + '=Unknown'
        else:
            return ip_address + '=Local'


class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    account_type = serializers.CharField(required=False)
    channel = serializers.CharField(required=False)
    fcmb_token = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    privacy = serializers.BooleanField(required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        privacy = attrs.get('privacy')

        if not email:
            raise serializers.ValidationError({"email": "Email is required"})
        if not password:
            raise serializers.ValidationError({"password": "Password is required"})
        if not privacy:
            raise serializers.ValidationError({"privacy": "You Must agree to our Privacy Terms"})

        return attrs

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        account_type = validated_data.get('account_type')
        channel = validated_data.get('channel')
        fcmb_token = validated_data.get('fcmb_token')
        username = validated_data.get('username')
        user = UserService().create_user(
            email=email, password=password, account_type=account_type, channel=channel, fcmb_token=fcmb_token,
            username=username
        )
        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )
    remember_me = serializers.BooleanField(default=False, write_only=True)
    device_name = serializers.CharField(max_length=255, allow_blank=False, required=True)
    device_id = serializers.CharField(max_length=255, allow_blank=False, required=True)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    device_name = serializers.CharField(max_length=255, allow_blank=False, required=True)
    device_id = serializers.CharField(max_length=255, allow_blank=False, required=True)
    user = serializers.CurrentUserDefault()

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password does not match.")
        return value

    def validate_new_password(self, value):
        user = self.context["request"].user
        try:
            validate_password(value, user)
            policy = PasswordPolicy.from_names(
                lenght=8, uppercase=1, strength=0.3, entropybits=1, nonletterslc=1, numbers=1, symbols=1, special=1, nonletters=1
            )
            policy.test(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value


class SendResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.EmailField()
    new_password = serializers.CharField(required=True)


class ContactUsSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()

    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'phone_number', 'message')


class LinkedInLoginSerializer(serializers.Serializer):
    token = serializers.CharField()
    user_id = serializers.IntegerField()
    email = serializers.EmailField()
    device_name = serializers.CharField(max_length=255, allow_blank=False, required=True)
    device_id = serializers.CharField(max_length=255, allow_blank=False, required=True)


class FacebookConnectSerializer(serializers.Serializer):
    access_token = serializers.CharField(required=True)
    device_name = serializers.CharField(max_length=255, allow_blank=False, required=True)
    device_id = serializers.CharField(max_length=255, allow_blank=False, required=True)
