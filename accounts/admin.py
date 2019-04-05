from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.UserProfile)
# admin.site.site_header = 'My Administration'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')

admin.site.register(models.UserProfile, UserProfileAdmin)