# from django.db import models
# from django.utils.crypto import get_random_string
# from django.utils import timezone
# from apps.users.models import CustomUser


# class Post(models.Model):
#     user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     content = models.TextField()
#     photo = models.ImageField(upload_to="post_images/", blank=True, null=True)
#     slug = models.SlugField(default="", unique=True)
#     is_hidden = models.BooleanField(default=False)
#     likes = models.ManyToManyField(
#         CustomUser,
#         related_name="post_likes",
#         symmetrical=False,
#     )
#     hashtags = models.ManyToManyField(
#         Hashtag,
#         related_name="post_hashtags",
#         symmetrical=False,
#     )

#     def __str__(self):
#         return self.content

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.slug = create_slug()

#         return super(Post, self).save(*args, **kwargs)


# class Reply(models.Model):
#     comment_id = models.ForeignKey(
#         Comment, on_delete=models.CASCADE, related_name="comment_replied"
#     )
#     user_id = models.ForeignKey(
#         CustomUser, on_delete=models.CASCADE, related_name="user_replied"
#     )
#     content = models.TextField()

#     def __str__(self):
#         return self.content


# def create_slug():
#     slug = get_random_string(10, "0123456789abcdefghijklmnopqrstuvwxyz")
#     return slug
