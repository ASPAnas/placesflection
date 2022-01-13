from django.contrib import admin

from .models import Memory, UserSocialMetadata


admin.site.register(Memory)
admin.site.register(UserSocialMetadata)
