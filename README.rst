
To test
=======

Start mongodb locally (currently configured to 127.0.0.1:27017
Start the task consumer (worker) as
         celery worker -A tasks
The system is ready for accepting tasks
         python test.py




