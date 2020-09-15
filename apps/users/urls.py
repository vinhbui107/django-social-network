from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views

from apps.users.views import (
    LoginView,
    SignupView,
    ActivateAccountView,
    ActivationSentView,
    ActivationInvalidView,
    ActivationSuccessView,
)

from .forms import LoginForm
from django.conf.urls.static import static

app_name = "users"

urlpatterns = [
    # login and logout
    path("login/", LoginView.as_view(form_class=LoginForm), name="login",),
    path("logout/", auth_views.LogoutView.as_view(), name="logout",),
    # register account
    path("signup/", SignupView.as_view(), name="signup"),
    path(
        "activate/<uidb64>/<token>/",
        ActivateAccountView.as_view(),
        name="activate",
    ),
    path("activate/sent/", ActivationSentView.as_view(), name="activate_sent"),
    path(
        "activate/invalid/",
        ActivationInvalidView.as_view(),
        name="activate_invalid",
    ),
    path(
        "activate/success/",
        ActivationSuccessView.as_view(),
        name="activate_success",
    ),
    # change password
    path(
        "change-password/",
        auth_views.PasswordChangeView.as_view(
            template_name="users/password_change.html"
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html"
        ),
        name="password_change_done",
    ),
    # reset password
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="users/password_reset.html"
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
