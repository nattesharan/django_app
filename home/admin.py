from django.contrib import admin
from home.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('user','created_on', 'post')
    def get_queryset(self, request):
        return super(PostAdmin, self).get_queryset(request).order_by('created_on')

admin.site.register(Post,PostAdmin)