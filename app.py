from flask import Flask
from api.data import data
from control_panel.dashboard import dashboard
import logging

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')

file_handler = logging.FileHandler('myLog.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

app = Flask(__name__)
app.secret_key = "super secret key"

app.logger.addHandler(file_handler)
app.logger.addHandler(stream_handler)
app.logger.setLevel(logging.INFO)

app.register_blueprint(data, url_prefix='/data')
app.register_blueprint(dashboard, url_prefix='/monitor')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

