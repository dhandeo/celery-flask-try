__author__ = 'dhan'

import flask
from tasks import add
from celery import Celery

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


app = flask.Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)

celery = make_celery(app)

@celery.task()
def add_together(a, b):
    return a + b

@app.route("/dashboard")
def dashboard():
    return flask.Response("Dashboard !")

@app.route("/")
def index():
    return flask.Response("try: <a href='" + flask.url_for('dashboard') + "'> Dashboard </a>")



