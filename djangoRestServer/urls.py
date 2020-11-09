from django.contrib import admin
from django.urls import include, re_path
from rest_framework.routers import SimpleRouter
from rest_framework_swagger.views import get_swagger_view

from users.api.auth_adapters import FacebookLogin, InstagramLogin


schema_view = get_swagger_view(title='App API')

router = SimpleRouter()
#  Register API routes using `router.register()`

api_version = 'api/v1'

urlpatterns = [
    # Admin
    re_path(r'^admin/', admin.site.urls, name='admin'),
    # Schema
    re_path(r'^$', schema_view),
    # API Endpoints
    re_path(r'^{0}/rest-auth/'.format(api_version), include('rest_auth.urls')),
    re_path(r'^{0}/rest-auth/registration/'.format(api_version), include('rest_auth.registration.urls')),
    re_path(r'^{0}/rest-auth/facebook/$'.format(api_version), FacebookLogin.as_view(), name='fb_login'),
    re_path(r'^{0}/rest-auth/instagram/$'.format(api_version), InstagramLogin.as_view(), name='instagram_login'),
    re_path(r'^{0}/accounts/'.format(api_version), include('users.api.urls')),
]
