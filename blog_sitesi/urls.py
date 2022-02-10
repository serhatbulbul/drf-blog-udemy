from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/yazi/', include('yazi.api.urls', namespace='yazi')),
    path('api/yorum/', include('yorum.api.urls', namespace='yorum')),
    path('sentry-debug/', trigger_error),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
