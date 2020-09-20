from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.posts.models import Post, Reply, Comment
from apps.users.models import CustomUser


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = "users:login"
    template_name = "core/home.html"
    redirect_field_name = "redirect_to"

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, self.template_name, {"posts": posts})
