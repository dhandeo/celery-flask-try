
Celery experiments
==================


To submit 3 asynchronous tasks, and to continuously poll for their progress use

::

   python test.py


But the tasks wont be consumed i.e. started and progressed leading to completion unless the worker is started using the command

::

   celery workder -A tasks

This command will start worker celery process which can consume all tasks defined in module tasks (tasks.py)
