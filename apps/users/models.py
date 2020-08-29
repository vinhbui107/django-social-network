from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):

    email = models.EmailField(
        verbose_name="email address", max_length=255, unique=True,
    )
    username = models.CharField(max_length=40, unique=True)
    display_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=16, blank=True)
    photo = models.ImageField(upload_to="user_images/", blank=True)
    google_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.email


class Follow(models.Model):
    follower_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_follower"
    )
    following_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_following"
    )
