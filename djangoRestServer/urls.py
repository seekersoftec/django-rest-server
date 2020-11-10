from django.contrib import admin
from django.urls import include, re_path
from rest_framework import routers, permissions
# 
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# 
from users.api.auth_adapters import FacebookLogin, InstagramLogin

# 
api_version = 'api/v1'

# 
schema_view = get_schema_view(
   openapi.Info(
      title="REST App API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = routers.SimpleRouter()
#  Register API routes using `router.register()`

# Admin
# router.register(r'^admin/', admin.site.urls, name='admin')
# Schema
# router.register(r'^$', schema_view)
# API Endpoints
# router.register(r'^{0}/rest-auth/'.format(api_version), include('rest_auth.urls'))


# Admin
admin_urls = [
    re_path(r'^admin/', admin.site.urls, name='admin'),
]

# Swagger
swagger_urls = [
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
    
  
# API Endpoints  
api_urls = [
    re_path(r'^{0}/rest-auth/'.format(api_version), include('rest_auth.urls')),
    re_path(r'^{0}/rest-auth/registration/'.format(api_version), include('rest_auth.registration.urls')),
    re_path(r'^{0}/rest-auth/facebook/$'.format(api_version), FacebookLogin.as_view(), name='fb_login'),
    re_path(r'^{0}/rest-auth/instagram/$'.format(api_version), InstagramLogin.as_view(), name='instagram_login'),
    re_path(r'^{0}/accounts/'.format(api_version), include('users.api.urls')),
]

# 
urlpatterns = []
urlpatterns += admin_urls + swagger_urls