#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if 'test' in sys.argv:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.test_settings")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)

# we can run the server with pyhton manage.py runserver
# we can also use ./manage.py runserver
# we can also use python -m django runserver but for this we need to have ENV variabale set
# we can also use django-admin runserver but for this we need to have ENV variabale set
# export DJANGO_SETTINGS_MODULE=django_app.settings and also export the python path export PYTHONPATH=. or source the env.sh file


#pytest --reuse-db --cov --nomigrations

# python -m smtpd -n -c DebuggingServer localhost:1025

# Permissions
# Assigning permissions to a user grants the user access to do what is described by those permissions. 
# When you create a user, that user has no permissions, and it’s up to you to give the user specific permissions. 
# For example, you can give a user permission to add and change publishers, but not permission to delete them.
# by default when we add a model it creates 3 permissions add, change and delete
# we can also use groups to group multiple permissions
# we check is a user has permission using obj.has_perm('perm') where perm is permission name (here the obj may be group or user)
# like 'app_name.action_model'
# we can alsoadd our own permissions in the model it is a tuple of tuples and then run migration
# if we want to use group we can add permissons to a group and add that group to user
# we can create a manage.py command for populationg the default groups


# python manage.py runscript script_name


# Starting the app with gunicorn
# gunicorn django_app.wsgi:application --bind=0.0.0.0:8000 --log-level info --access-logfile django_app.log --error-logfile app_errors.log --pid django_app.pid