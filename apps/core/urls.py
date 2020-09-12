from django.urls import path
from apps.core.views import HomeView
from django.conf import settings
from django.conf.urls.static import static

app_name = "core"

urlpatterns = [path("", HomeView.as_view(), name="home")] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
