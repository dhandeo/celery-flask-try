Celery experiments
==================

Start mongodb locally (currently configured to 127.0.0.1:27017

To submit 3 asynchronous tasks, and to continuously poll for their progress use

::

   python test.py


But the tasks wont be consumed i.e. started and progressed leading to completion unless the worker is started using the command

::

   celery workder -A tasks
