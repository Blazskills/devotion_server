from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view as swagger_get_schema_view

from rest_framework import authentication, permissions


class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        """Generate a :class:`.Swagger` object with custom tags"""

        swagger = super().get_schema(request, public)

        return swagger


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Devotion+ Api",
        default_version="v1",
        description="API Documentation of Devotion Application",
        contact=openapi.Contact(email="info@devotion.com"),
    ),
    public=True,
    authentication_classes=[authentication.SessionAuthentication],
    permission_classes=[permissions.IsAuthenticated],
    generator_class=CustomOpenAPISchemaGenerator,
)

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path(
        "api/v1/",
        include(
            [
                # path("account/", include("core_apps.account.urls")),
                path("devotion/", include("core_apps.devotion.urls")),
                path(
                    "swagger/schema/",
                    schema_view.with_ui("swagger", cache_timeout=0),
                    name="swagger-schema",
                ),
                path(
                    "redoc/",
                    schema_view.with_ui("redoc", cache_timeout=0),
                    name="schema-redoc",
                ),
            ]
        ),
    ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Devotion API Admin"

admin.site.site_title = "Devotion API Admin Portal"

admin.site.index_title = "Welcome to Devotion API Portal"
