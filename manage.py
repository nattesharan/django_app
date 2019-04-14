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