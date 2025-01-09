# recipes/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    Fixes applied to avoid reverse accessor conflicts.
    """
    age = models.PositiveIntegerField(null=True, blank=True)

    # Fixed related_name conflicts with unique names
    groups = models.ManyToManyField(
        'auth.Group',
        related_name="user_custom_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="user_custom_permissions",
        blank=True
    )

    class Meta:
        permissions = [('can_view_dashboard', 'Can view the dashboard')]


class Recipe(models.Model):
    """
    Recipe model storing detailed recipe information.
    Linked to the custom User model.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.JSONField()
    instructions = models.TextField()
    category = models.CharField(max_length=100)
    preparation_time = models.PositiveIntegerField()
    cooking_time = models.PositiveIntegerField()
    servings = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
