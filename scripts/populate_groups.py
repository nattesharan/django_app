from django.db import transaction
from django.contrib.auth.models import Group, Permission, User
# Atomicity is the defining property of database transactions. 
# atomic allows us to create a block of code within which the atomicity on the database is guaranteed. 
# If the block of code is successfully completed, the changes are committed to the database. 
# If there is an exception, the changes are rolled back.
@transaction.atomic
def run():
    '''
    We use groups to group a set of permissions so instead of checking multiple permissions
    we can check if user is part of group
    Usecase: Roles where the permissions are grouped to a role which a user is assigned
    '''
    exclude_perms = ['add_post', 'change_post']
    # this creates in bulk but not recommened because it doesnt handle get_or_create
    # scripts should be written in such a way that it will ensure the database consistency even if run multiple times
    # groups = Group.objects.bulk_create(
    #     [
    #         Group(name='NORMAL_USER'),
    #         Group(name='ADMIN_USER')
    #     ]
    # )
    users = User.objects.all()
    for group_name in ['NORMAL_USER','ADMIN_USER']:
        group, status = Group.objects.get_or_create(name=group_name)
        if group_name == 'NORMAL_USER':
            permissions = Permission.objects.filter(codename__in=exclude_perms)
        if group_name == 'ADMIN_USER':
            permissions = Permission.objects.all()
        for permission in permissions:
            if permission not in group.permissions.all():
                # add the permission to the group if not exists
                group.permissions.add(permission)
    for user in users:
        if user.is_superuser:
            group = Group.objects.get(name='ADMIN_USER')
        else:
            group = Group.objects.get(name='NORMAL_USER')
        if group not in user.groups.all():
            user.groups.add(group)
        