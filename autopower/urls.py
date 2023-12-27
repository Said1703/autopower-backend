from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Autopower api",
        default_version="v1",
        description="API sobre Autopower, seguros vehiculares",
        licence=openapi.License(name="MTI")
    ),
    public=True,
    permission_classes=(AllowAny,)
)

api_version = "api/v1/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(api_version, include("user.urls")),
    path(api_version, include("buyer.urls")),
    path(api_version, include("subscription.urls")),
    path("swagger/", schema_view.with_ui("swagger",
         cache_timeout=0), name="schema-swagger-url")
]
