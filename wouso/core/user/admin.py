from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as OldUserAdmin
from wouso.core.user.models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserAdmin(OldUserAdmin):
    inlines = [ UserProfileInline ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)