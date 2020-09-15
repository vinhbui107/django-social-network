from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import LoginView
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.conf import settings
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.models import Site


from .forms import SignupForm, LoginForm
from .tokens import account_activation_token


class LoginView(LoginView):
    template_name = "users/login.html"
    form_class = LoginForm


class SignupView(CreateView):
    template_name = "users/signup.html"
    form_class = SignupForm

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.is_active = False
            user.save()

            current_site = request.get_host()
            subject = "Activate Your Djangram Account"
            message = render_to_string(
                "emails/account_activation_email.html",
                {
                    "user": user,
                    "domain": current_site,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            mail = EmailMessage(
                subject,
                message,
                to=[user.email],
                from_email=settings.EMAIL_HOST_USER,
            )
            mail.send()
            return redirect("users:activate_sent")

        else:
            return render(request, self.template_name, {"form": form})


class ActivateAccountView(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        User = get_user_model()
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(
            user, token
        ):
            user.is_active = True
            user.save()
            messages.success(request, ("Your account have been confirmed."))
            return redirect("users:activate_success")
        else:
            messages.warning(
                request,
                (
                    "The confirmation link was invalid, possibly because it has already been used."
                ),
            )
            return redirect("users:activate_invalid")


class ActivationSentView(TemplateView):
    template_name = "users/activation_sent.html"


class ActivationSuccessView(TemplateView):
    template_name = "users/activation_success.html"


class ActivationInvalidView(TemplateView):
    template_name = "users/activation_invalid.html"
