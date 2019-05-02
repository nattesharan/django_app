from rest_framework.permissions import BasePermission

class ListPermission(BasePermission):
    def has_permission(self, request, view):
        url_name = request.resolver_match.url_name
        if request.method == 'GET' and url_name in ['generic_posts_get']:
            if not request.user.is_superuser:
                return False
            return True
        return True