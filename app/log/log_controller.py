from flask import Blueprint, render_template
from app.log.db_log import findAllLog

log_controller = Blueprint('log_controller', __name__, template_folder='templates')

@log_controller.route('/')
def show_recent_log():
    result = findAllLog()
    return render_template('log_list.html', logSet = result)