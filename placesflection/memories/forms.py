from django.forms import ModelForm
from .models import Memory


class MemoryForm(ModelForm):
    """Form validating Memory objects."""

    class Meta:
        model = Memory
        fields = ["title", "description", "location"]
