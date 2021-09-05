from django.contrib import admin

from accounts.models import UserProfile, Follow

admin.site.register(UserProfile)
admin.site.register(Follow)