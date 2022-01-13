from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField


class Memory(models.Model):
    """Single place memory representation."""

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = PlainLocationField(based_fields=["city"], zoom=7)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
