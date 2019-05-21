from flask import Blueprint, render_template, url_for, redirect, flash
from flask import current_app as app
from flask_login import login_required

from app.control_panel.model import RFCItem
# import app.control_panel.share_data as shareData
# from app.control_panel.share_data import rfcCallName, rfcCallDesc
from app.control_panel.share_data import environments
from app.utils.time_format import pretty_date

dashboard = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard.route('/<env>')
# @login_required
def monitorDataList(env):
    if environments[env].last_update:
        last_update = pretty_date(environments[env].last_update)
    else:
        last_update = 'Data uploading...'
    return render_template('monitor_list.html', env = environments[env], last_update = last_update)

@dashboard.route('/<log_id>/<variante>/<env>')
# @login_required
def monitorDataDetail(log_id, variante, env):
    item = findByIDAndVar(log_id, variante, env)
    if item:
        last_update = pretty_date(environments[env].last_update)
        app.logger.info(item)
        return render_template('monitor_detail.html',
                               env = environments[env],
                               data = item,
                               last_update = last_update)
    else:
        return redirect(url_for('dashboard.monitorDataList', env = env))

@dashboard.route('/rfc_call/<rfc_type>/<log_id>/<variante>/<env>')
# @login_required
def rfcCallChar(rfc_type, log_id, variante, env):
    if not environments[env].rfcCallName.get(rfc_type):
        flash(f'RFC Call is not defined', 'error')
        return render_template('flash_message.html')
    if environments[env].rfcCall.status == 'ready':
        result = findByIDAndVar(log_id, variante, env)
        if result:
            rfcItem =  RFCItem(result)
            rfcItem.rfcName = environments[env].rfcCallName[rfc_type]
            json_str = rfcItem.serialize()
            if json_str:
                environments[env].rfcCall.rfcItem = rfcItem
                environments[env].rfcCall.env = env
                environments[env].rfcCall.setRFCCall(json_str)
            else:
                flash('RFC Call key error.')
                return render_template('flash_message.html')
            flash('Executing...', 'info')
            print('RFC Call ' + rfcItem.rfcName + ' is being executed.')
        else:
            flash('The data is no longer available. Please refresh data.', 'warning')
    else:
        flash('RFC call in process. Please try again later.', 'warning')
    return render_template('flash_message.html')

def findByIDAndVar(log_id, variante, env):
    result = None
    for item in environments[env].monitorData:
        if item['LOG_ID'] == log_id and item['VARIANTE'] == variante:
            result = item
            break
    if result:
        return result
    else:
        return None

@dashboard.route('/last_update/<env>')
def updateLastUpdate(env):
    if env == 'undefined':
        return ""
    if not environments[env].last_update:
        return 'Data uploading...'
    last_update = pretty_date(environments[env].last_update)
    if "minute" in last_update or "hours" in last_update or "days" in last_update:
        return "Data may be outdated. Click to Refresh."
    else:
        return pretty_date(environments[env].last_update)