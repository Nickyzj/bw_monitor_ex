from flask import Blueprint, render_template
from app.log.db_log import findAllLog, findLogById

log_controller = Blueprint('log_controller', __name__, template_folder='templates')

@log_controller.route('/')
def show_recent_log():
    result = findAllLog()
    return render_template('log_list.html', logSet = result)

@log_controller.route('/<id>')
def show_log_detail(id):
    result = findLogById(id)
    print(result['LOG_ID'])
    return render_template('log_detail.html', logItem = result)