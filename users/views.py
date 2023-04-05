import logging
from collections import OrderedDict
from datetime import timedelta

import requests
from allauth.account.models import EmailAddress
from allauth.socialaccount import providers
from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialToken, SocialLogin
from allauth.socialaccount.providers.base import AuthError
from allauth.socialaccount.providers.facebook.provider import FacebookProvider, GRAPH_API_URL
from allauth.socialaccount.providers.facebook.views import fb_complete_login
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.linkedin.views import LinkedInOAuthAdapter
from django.conf import settings
from django.db.models import F
from django.utils import timezone
from facebook import GraphAPI
from google.auth.credentials import Credentials
from googleapiclient.discovery import build
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.throttling import SimpleRateThrottle
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.models import Plan, SystemPlanDiscount, Testimonials, Blog, FAQ, Newsletter, User, SystemContact, ContactUs
from users.serializers import (
    ChangePasswordSerializer,
    ResetPasswordSerializer,
    SendResetPasswordEmailSerializer,
    SignupSerializer, PlanSerializer, SystemPlanDiscountSerializer, TestimonialSerializer, BlogSerializer,
    FAQSerializer, NewsletterSerializer, AuthTokenSerializer, SystemContactSerializer, ContactUsSerializer,
    FullBlogSerializer, LinkedInLoginSerializer, FacebookConnectSerializer,
)
from users.services import AuthenticationService

LOG = logging.getLogger(__name__)


class ChangePasswordAPIView(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            token = AuthenticationService.change_password(**serializer.validated_data)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordEmailAPIView(GenericAPIView):
    serializer_class = SendResetPasswordEmailSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        AuthenticationService.setup_reset_password(**serializer.validated_data)

        return Response(
            {"message": "Please, Check your mail."}, status=status.HTTP_200_OK
        )


class PasswordResetView(GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def get(self, request, token):
        if AuthenticationService.check_reset_token(token):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if AuthenticationService.reset_password(**serializer.validated_data):
            return Response({"message": "Password reset successful."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view=None):
        if request.method in SAFE_METHODS:
            return True
        return request.user and (request.user.is_staff or request.user.is_superuser)


class IsUserOrReadOnly(BasePermission):
    def has_permission(self, request, view=None):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user)


class PermissionMixinAdmin:
    pagination_class = LimitOffsetPagination
    pagination_class.default_limit = 9
    pagination_class.limit_query_param = 'page_size'
    pagination_class.offset_query_param = 'page'

    def get_permissions(self):
        permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
        if self.action in ['create', 'post', 'delete']:
            permission_classes = [IsAdminOrReadOnly(), ]
        return permission_classes


class PermissionMixinUser(PermissionMixinAdmin):
    def get_permissions(self):
        permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
        if self.action in ['create', 'post']:
            permission_classes = [IsUserOrReadOnly(), ]
        elif self.action in ['delete']:
            permission_classes = [IsAdminOrReadOnly, ]
        return permission_classes


class PlanViewSet(PermissionMixinAdmin, ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class SystemPlanDiscountViewSet(PermissionMixinAdmin, ModelViewSet):
    queryset = SystemPlanDiscount.objects.filter(pk=1)
    serializer_class = SystemPlanDiscountSerializer

    def get_object(self):
        return SystemPlanDiscount.load()


class TestimonialViewSet(PermissionMixinUser, ModelViewSet):
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        queryset = Testimonials.objects.filter(ratings__gt=F('ratings') * 100 - 30)
        return queryset.order_by('-created')


class BlogViewSet(PermissionMixinAdmin, ModelViewSet):
    serializer_class = BlogSerializer
    filterset_fields = ['slug']
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        return Blog.objects.order_by('-created')


class FullBlogViewSet(PermissionMixinAdmin, ModelViewSet):
    serializer_class = FullBlogSerializer
    filterset_fields = ['slug']
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        return Blog.objects.order_by('-created')


class FAQViewSet(PermissionMixinAdmin, ModelViewSet):
    serializer_class = FAQSerializer

    def get_queryset(self):
        return FAQ.objects.order_by('-created')


class CustomThrottle(SimpleRateThrottle):
    scope = 'custom'
    rate = '10/day'

    def get_cache_key(self, request, view):
        return self.get_ident(request)


class ThrottleMixin:
    throttle_classes = [CustomThrottle]

    def get_throttles(self):
        if self.request.user and self.request.user.is_authenticated:
            self.throttle_classes = []
        return [throttle() for throttle in self.throttle_classes]


class NewsletterViewSet(ThrottleMixin, ModelViewSet):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer


class CreateUserView(ThrottleMixin, CreateAPIView):
    serializer_class = SignupSerializer


class LoginView(ObtainAuthToken):
    """
        import requests

        data = {
            "email": "user@example.com",
            "password": "password",
            "remember_me": True,
            "device_name":"Windows",
            "device_id":"12345"
        }
        headers = {
            "Device-Name": "Windows",
            "Device-Id":"12345"
        }
        response = requests.post('http://localhost:8000/login/', json=data, headers=headers)

    """
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        device_name = request.headers.get("Device-Name", None)
        device_id = request.headers.get("Device-Id", None)
        request.data.update({"device_name": device_name, "device_id": device_id})
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        remember_me = serializer.validated_data.get('remember_me', False)
        device_name = serializer.validated_data.get('device_name', None)
        device_id = serializer.validated_data.get('device_id', None)
        token, created = Token.objects.get_or_create(user=user)
        user.logged_devices.create(device_name=device_name, device_id=device_id, token=token)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'device_name': device_name,
        })


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Remove the device from the user's logged_devices list
        device_name = request.headers.get("Device-Name")
        device_id = request.headers.get("Device-Id")
        device = request.user.logged_devices.filter(device_name=device_name, device_id=device_id).first()
        if device:
            device.delete()
            return Response({"message": "Device successfully logged out."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Device not found."}, status=status.HTTP_404_NOT_FOUND)


class GoogleClientIdView(APIView):
    def get(self, request):
        client_id = settings.GOOGLE_CLIENT_ID
        return Response({"client_id": client_id})


class SystemContactViewSet(PermissionMixinAdmin, ModelViewSet):
    queryset = SystemContact.objects.filter(pk=1)
    serializer_class = SystemContactSerializer

    def get_object(self):
        return SystemContact.load()


class ContactUsViewSet(ThrottleMixin, ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class AllAuthLinkedInLoginView(LoginView):
    serializer_class = LinkedInLoginSerializer
    adapter_class = LinkedInOAuthAdapter


class AllAuthGoogleLoginView(LoginView):
    serializer_class = LinkedInLoginSerializer
    adapter_class = GoogleOAuth2Adapter


class SocialProvider(ThrottleMixin, APIView):
    def get(self, request):
        providers_ = OrderedDict()
        [providers_.setdefault(provider_cls.name, provider_cls.id)
         for provider_cls in providers.registry.provider_map.values()]
        return Response(providers_, status=status.HTTP_200_OK)


class ExchangeSessionForToken(APIView):
    def get(self, request):
        # Check if the user is authenticated using a session
        if request.user.is_authenticated:
            token, created = Token.objects.get_or_create(user=request.user)
            request.user.logged_devices.create(device_name='TraffikBoss Exchange', device_id='API TraffikBoss', token=token)
            try:
                email = EmailAddress.objects.get(user=request.user).email
            except EmailAddress.DoesNotExist:
                email = request.user.email if request.user.email else 'Please set your email'

            return Response({
                'token': token.key,
                'user_uid': request.user.pk,
                'email': email,
                'device_name': 'TraffikBoss Exchange',
                # 'expires': token.expires,
            })
        else:
            # If the user is not authenticated, return an error response
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)