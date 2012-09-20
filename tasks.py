from __future__ import absolute_import
import time
from celery import Celery, current_task
#from tasks import add

celery = Celery(broker="mongodb://127.0.0.1/celery", backend="mongodb://127.0.0.1/celery")
#celeryapp.config_from_object()

@celery.task(name="tasks.add")
def add(x, y):
    print "Starting job ..", x, y 
    for i in range(x):
        time.sleep(1)
        current_task.update_state(state='PROGRESS', meta=str({'current': i, 'total': x}))
        
        # Alternate try
        #add.backend.store_result(task_id, state='PROGRESS', result={'current': i, 'total': x}, traceback=None)
        print str({'current': i, 'total': x})
        # Update progress 
    return y


if __name__ == '__main__':
    celery.start()





















