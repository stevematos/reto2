# RETO 2 - CREHANA
## Quick Start
```shell script
$ pip install --upgrade virtualenv
$ virtualenv env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
(env) $ python manage.py loaddata initial_data.json
(env) $ python manage.py migration_progress_video
```
El command migration_progress_video tambien se puede ingresar los ids que se desea migrar.
```
(env) $ python manage.py migration_progress_video -i 1 2 3
```