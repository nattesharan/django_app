from django.contrib.admin.models import LogEntry, ADDITION, ContentType
from functools import wraps
from rest_framework.response import Response
# this function takes list of permissions and checks if the entity has the list of permissions
def has_model_permissions( entity, perms, app):
    for p in perms:
        if not entity.has_perm( "%s.%s" % ( app, p) ):
            return False
        return True


def add_permissions(permissions, user, admin_user):
    for permission in permissions:
        # if theres no permission for that user add it
        if not has_model_permissions(user, [permission.codename], 'home'):
            user.user_permissions.add(permission)
            try:
                LogEntry.objects.log_action(
                    user_id=admin_user.pk,
                    content_type_id=ContentType.objects.get_for_model(user).pk,
                    object_id=user.id,
                    object_repr=user.get_full_name(),
                    action_flag=ADDITION,
                    change_message="Added Permission"
                )
            except Exception as E:
                print(E)
    return True

def check_permission(permission):
    def decorator(view_func):
        @wraps(view_func)
        def decorated(request, *args, **kwargs):
            app, perm = permission.split('.')
            if has_model_permissions(request.user, [perm], app):
                return view_func(request, *args, **kwargs)
            return Response({'message': 'You dont have permission to do this'}, status=401)
        return decorated
    return decorator