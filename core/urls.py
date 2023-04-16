from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from core.schema import swagger_urlpatterns


def trigger_error(request):
    division_by_zero = 1 / 0  # noqa


urlpatterns = [
    path("api/v1/sentry/TriggerError", trigger_error),
    path("admin/", admin.site.urls),
    # path("api/v1/users/", include("apps.users.urls")),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
