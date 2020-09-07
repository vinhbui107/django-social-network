from django.urls import path
from apps.core.views import HomeView

app_name = "core"


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
