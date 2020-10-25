from django.db import models
from apps.users.models import CustomUser
from django.utils.crypto import get_random_string
from django.utils import timezone


class Post(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    photo = models.ImageField(upload_to="post_images/", blank=True)
    slug = models.SlugField(default="", unique=True)
    is_hidden = models.BooleanField(default=False)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    likes = models.ManyToManyField(
        CustomUser, related_name="like_users", blank=True, symmetrical=False,
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = create_slug()
            self.created_date = timezone.now()

        self.updated_date = timezone.now()
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post_id = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_commented"
    )
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_commented"
    )
    content = models.TextField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_date = timezone.now()

        self.updated_date = timezone.now()
        return super(Comment, self).save(*args, **kwargs)


class Reply(models.Model):
    comment_id = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="comment_replied"
    )
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_replied"
    )
    content = models.TextField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_date = timezone.now()

        self.updated_date = timezone.now()
        return super(Reply, self).save(*args, **kwargs)


def create_slug():
    slug = get_random_string(10, "0123456789abcdefghijklmnopqrstuvwxyz")
    return slug
