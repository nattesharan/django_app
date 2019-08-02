from django.contrib import admin
from home.models import Post
from django.contrib.auth.models import User
# Register your models here.

# The problem with search fields Django Admin search fields are great — throw a bunch of fields in search_fields and 
# Django will handle the rest.
# The problem with search field begins when there are too many of them.
# When the admin user want to search by UID or email, Django has no idea this is what the user intended so it has 
# to search by all the fields listed in search_fields. These “match any” queries have huge WHERE clauses and lots of 
# joins and can quickly become very slow.
class UsersListFilter(admin.SimpleListFilter):
    """
    This filter will always return a subset of the instances in a Model, either filtering by the
    user choice or by a default value.
    """
    title = 'Users'
    parameter_name = 'user'
    default_value = None

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        list_of_users = []
        queryset = User.objects.all()
        for user in queryset:
            list_of_users.append((str(user.id), user.username))
        return sorted(list_of_users, key=lambda tp: tp[1])
    
    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value to decide how to filter the queryset.
        if self.value():
            return queryset.filter(user_id=self.value())
        return queryset

class PostAdmin(admin.ModelAdmin):
    search_fields = ('post', 'user__username', 'id',)
    list_display = ('user','created_on', 'post')
    list_filter = (UsersListFilter, )
    def get_queryset(self, request):
        return super(PostAdmin, self).get_queryset(request).order_by('created_on')

admin.site.register(Post,PostAdmin)