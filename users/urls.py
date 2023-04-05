from django.urls import path, include
from rest_framework import routers

from users.views import PlanViewSet, SystemPlanDiscountViewSet, BlogViewSet, FAQViewSet, NewsletterViewSet, \
    CreateUserView, PasswordResetView, LoginView, SystemContactViewSet, ContactUsViewSet, FullBlogViewSet, \
    TestimonialViewSet, SocialProvider, ExchangeSessionForToken

router = routers.DefaultRouter()
router.register(r'plans', PlanViewSet, basename='plans')
router.register(r'plan-discount-yearly', SystemPlanDiscountViewSet, basename='plan-discount-yearly')
router.register(r'testimonials', TestimonialViewSet, basename='testimonials')
router.register(r'home-blog', BlogViewSet, basename='home-blog')
router.register(r'blog', FullBlogViewSet, basename='blog')
router.register(r'home-faq', FAQViewSet, basename='home-faq')
router.register(r'newsletter', NewsletterViewSet, basename='newsletter')
router.register(r'system-contact', SystemContactViewSet, basename='system-contact')
router.register(r'contact', ContactUsViewSet, basename='contact')


urlpatterns = [
    path('', include(router.urls)),
    path('providers/', SocialProvider.as_view(), name='providers'),
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('login/', LoginView.as_view(), name='login'),
    path('exchange/', ExchangeSessionForToken.as_view(), name='exchange_session_for_token'),
]
