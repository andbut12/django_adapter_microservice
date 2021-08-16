"""example_eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from apps.cargo.views import CargoViewSet
from apps.geo.views import GeoViewSet
from apps.rates.views import RateViewSet
from apps.shipments.views import ShipmentViewSet
from apps.users.views import ContactViewSet

admin.autodiscover()
admin.site.enable_nav_sidebar = False


class SchemeGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ['https', 'http']
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce API",
        default_version='v1',
        description="E-Commerce API",
        terms_of_service="https://example.ru/privacy/",
        contact=openapi.Contact(email="dev@example.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=SchemeGenerator,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

router = routers.DefaultRouter(trailing_slash=False)

# FYI: не включать, т.к. токены бесконечные
# router.register(r'authentication', SignInViewSet, basename='authentication')

router.register(r'geo', GeoViewSet, basename='geo')
router.register(r'contact', ContactViewSet, basename='contact')
router.register(r'cargo', CargoViewSet, basename='cargo')
router.register(r'rate', RateViewSet, basename='rate')
router.register(r'shipment', ShipmentViewSet, basename='shipment')

urlpatterns += router.urls
