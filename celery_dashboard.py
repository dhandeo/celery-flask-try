__author__ = 'dhan'

import flask
from tasks import add
from celery import Celery
from celery.task.control import inspect

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
    CELERY_BROKER_URL='mongodb://127.0.0.1/celery',
    CELERY_RESULT_BACKEND='mongodb://127.0.0.1/celery'
)

celery = make_celery(app)


def get_celery_worker_status():
    ERROR_KEY = "ERROR"
    try:
        insp = celery.control.inspect()
        d = insp.stats()
        r = insp.registered()
        if not d:
            d = { ERROR_KEY: 'No running Celery workers were found.' }
    except IOError as e:
        from errno import errorcode
        msg = "Error connecting to the brocker: " + str(e)
        if len(e.args) > 0 and errorcode.get(e.args[0]) == 'ECONNREFUSED':
            msg += ' Check that the RabbitMQ server is running.'
        d = { ERROR_KEY: msg }
    except ImportError as e:
        d = { ERROR_KEY: str(e)}
    return {"stats" : d, "registered" : r}


@celery.task()
def add_together(a, b):
    return a + b

@app.route("/dashboard")
def dashboard():
    status = get_celery_worker_status()
    print status
    return flask.render_template("dashboard.html", workers= [status["registered"],],tasks = [])

@app.route("/")
def index():
    return flask.Response("try: <a href='" + flask.url_for('dashboard') + "'> Dashboard </a>")



