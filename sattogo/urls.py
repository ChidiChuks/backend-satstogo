"""
URL configuration for sattogo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.provider import GoogleProvider
from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView, OAuth2CallbackView


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleProvider.oauth2_adapter_class


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),  # Login, Logout, Password Reset
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # Registration
    path('auth/google/callback/', GoogleLogin.as_view(), name='google_login'),  # Google login
    path('api/', include('api.urls')),
    path('events/', include('events.urls')),
    path('wallet/', include('wallet.urls')),
]