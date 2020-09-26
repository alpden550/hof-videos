from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Custom user inherits from django user."""
