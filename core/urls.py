from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.urls import include, path

from core.schema import swagger_urlpatterns


def trigger_error(request):
    division_by_zero = 1 / 0  # noqa


class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def clean(self):
        cleaned_data = super().clean()
        captcha = cleaned_data.get("captcha")
        if not captcha:
            raise forms.ValidationError("Invalid captcha")
        return cleaned_data


admin.site.login_form = LoginForm
admin.site.login_template = "admin_login/login.html"

urlpatterns = [
    path("api/v1/sentry/TriggerError", trigger_error),
    path("admin/", admin.site.urls),
    # path('captcha/', include('captcha.urls')),
    path("api/v1/", include("apps.v1")),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
