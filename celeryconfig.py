#    Settings for Redis    
#    BROKER_URL = 'redis://localhost:6379/0'    
#    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
#  
# Settings for mongodb
#mongodb://userid:password@hostname:port/database_name

CELERY_RESULT_BACKEND = 'mongodb'
BROKER_HOST = "127.0.0.1"
BROKER_PORT = 27017
BROKER_TRANSPORT = 'mongodb'
BROKER_VHOST = 'celery'

CELERY_IMPORTS = ("tasks", )

CELERY_MONGODB_BACKEND_SETTINGS = { 
       'host': 'mongodb://127.0.0.1:27017/celery',
       #'database': 'celery',
       'taskmeta_collection': 'taskmeta'
       }   
