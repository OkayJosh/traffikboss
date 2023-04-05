"""traffikboss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from traffikboss.views import LogView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('account/', include('allauth.account.urls')),
    path('', include('linkedin_oauth2.urls')),
    path('post/', include('socials.urls')),
    path('logs/', LogView.as_view(), name='logs')
]


# to access social logins through the api
# POST request:http://127.0.0.1:8000/{provider}/login/?process=login
# i.e POST request:http://127.0.0.1:8000/linkedin/login/?process=login
