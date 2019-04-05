from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.UserProfile)
# admin.site.site_header = 'My Administration'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'user_info', 'website')

    def user_info(self, instance):
        return instance.description
    
    user_info.short_description = 'Description'
admin.site.register(models.UserProfile, UserProfileAdmin)