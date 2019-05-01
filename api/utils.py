from django.contrib.admin.models import LogEntry, ADDITION, ContentType

def add_permissions(permissions, user, admin_user):
    for permission in permissions:
        # if theres no permission for that user add it
        if not user.has_perm(permission.codename):
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