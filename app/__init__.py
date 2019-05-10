from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import logging

from app.forms import RegistrationForm, LoginForm

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

app.logger.addHandler(file_handler)
app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)

from app.api.data import data
from app.auth.routes import auth
from app.control_panel.dashboard import dashboard

app.register_blueprint(data, url_prefix='/data')
app.register_blueprint(dashboard, url_prefix='/monitor')
app.register_blueprint(auth)