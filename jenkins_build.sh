#!/bin/bash

set -e
export WORKSPACE=`pwd`
# Create/Activate virtualenv
virtualenv venv -p python3
source venv/bin/activate
# Install Requirements
pip install -r requirements.txt
# Run tests
python manage.py test
pytest --cov-report=xml -x -s
codecov
cd /home/nattesharan/django_app/
git pull origin master
source venv/bin/activate
pip install -r requirements.txt
sudo sonar-scanner -Dsonar.projectKey=django_app -Dsonar.sources=. -Dsonar.login=77208f48bdbff3b1855ccfe3db2d24823e6596fe
python manage.py migrate
sudo celery multi restart django_app -A django_app --pidfile="%n.pid" --loglevel=info --logfile='django_app.log'
sudo celery multi restart django_app_beat -A django_app --beat -c 1 --pidfile="%n.pid" --loglevel=info logfile="django_beat.log" --scheduler=django_celery_beat.schedulers:DatabaseScheduler
sudo supervisorctl restart django_app
whoami
