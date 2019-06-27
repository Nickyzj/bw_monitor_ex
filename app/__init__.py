from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from celery import Celery
import logging

# from app.auth.forms import RegistrationForm, LoginForm

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')

file_handler = logging.FileHandler('myLog.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

app.logger.addHandler(file_handler)
app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)

# Celery
app.config['CELERY_BROKER_URL'] = 'pyamqp://guest@localhost//'
app.config['CELERY_BACKEND'] = 'redis://localhost'
# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], backend=app.config['CELERY_BACKEND'])
def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'], backend=app.config['CELERY_BACKEND'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery
celery = make_celery(app)
# End of celery

from app.api.data import data
from app.auth.routes import auth
from app.control_panel.dashboard import dashboard
from app.log.log_controller import log_controller

app.register_blueprint(data, url_prefix='/data')
app.register_blueprint(dashboard, url_prefix='/monitor')
app.register_blueprint(log_controller, url_prefix='/log')
app.register_blueprint(auth)

@app.errorhandler(404)
def page_not_found(error):
    return redirect('/monitor/pcb')

