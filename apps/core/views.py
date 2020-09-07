from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = "/accounts/login"
    template_name = "core/home.html"
    redirect_field_name = "redirect_to"
