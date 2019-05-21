from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
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

from app.api.data import data
from app.auth.routes import auth
from app.control_panel.dashboard import dashboard
from app.log.log_controller import log_controller

app.register_blueprint(data, url_prefix='/data')
app.register_blueprint(dashboard, url_prefix='/monitor')
app.register_blueprint(log_controller, url_prefix='/log')
app.register_blueprint(auth)