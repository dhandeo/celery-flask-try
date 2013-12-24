Celery experiments
==================


Experiment 1
------------

Start mongodb locally (currently configured to 127.0.0.1:27017

To submit 3 asynchronous tasks, and to continuously poll for their progress use

::

   $ python test.py


But the tasks wont be consumed i.e. started and progressed leading to completion unless the worker is started using the command

::

   $ celery workder -A tasks

Experiment 2
------------

This requires flask and redis

Start the flask web server as

::

    $ celery -A celery_dashboard.celery worker
    $ python run.py

