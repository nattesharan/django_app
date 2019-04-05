from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.UserProfile)
# admin.site.site_header = 'My Administration'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'user_info', 'website')

    def user_info(self, instance):
        return instance.description
    
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        return queryset.order_by('-phone', 'user')
    
    user_info.short_description = 'Description'
admin.site.register(models.UserProfile, UserProfileAdmin)