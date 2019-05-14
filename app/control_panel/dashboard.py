from flask import Blueprint, render_template, url_for, redirect, flash
from flask import current_app as app
from flask_login import login_required

from app.control_panel.model import RFCItem
import app.control_panel.share_data as shareData
from app.control_panel.share_data import rfcCallName
from app.utils.time_format import pretty_date

dashboard = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard.route('/')
# @login_required
def monitorDataList():
    if shareData.last_update:
        last_update = pretty_date(shareData.last_update)
    else:
        last_update = 'Data uploading...'
    return render_template('monitor_list.html', data = shareData.monitorData, last_update = last_update)

@dashboard.route('/<log_id>/<variante>')
# @login_required
def monitorDataDetail(log_id, variante):
    item = findByIDAndVar(log_id, variante)
    if item:
        last_update = pretty_date(shareData.last_update)
        app.logger.info(item)
        return render_template('monitor_detail.html', data = item, last_update = last_update, commands = rfcCallName)
    else:
        return redirect(url_for('dashboard.monitorDataList'))

@dashboard.route('/rfc_call/<rfc_type>/<log_id>/<variante>')
# @login_required
def rfcCallChar(rfc_type, log_id, variante):
    if not rfcCallName.get(rfc_type):
        flash(f'RFC Call is not defined', 'error')
        return render_template('flash_message.html')
    if shareData.rfcCall.status == 'ready':
        result = findByIDAndVar(log_id, variante)
        if result:
            rfcItem =  RFCItem(result)
            rfcItem.rfcName = rfcCallName[rfc_type]
            shareData.rfcCall.setRFCCall(rfcItem.serialize())
            flash('RFC Call ' + rfcItem.rfcName + ' is being executed.', 'info')
            print('RFC Call ' + rfcItem.rfcName + ' is being executed.')
        else:
            flash('The data is no longer available. Please refresh data.', 'warning')
    else:
        flash('RFC call in process. Please try again later.', 'warning')
    return render_template('flash_message.html')

def findByIDAndVar(log_id, variante):
    result = None
    for item in shareData.monitorData:
        if item['LOG_ID'] == log_id and item['VARIANTE'] == variante:
            result = item
            break
    if result:
        return result
    else:
        return None

@dashboard.route('/last_update')
def updateLastUpdate():
    if not shareData.last_update:
        return 'Data uploading...'
    last_update = pretty_date(shareData.last_update)
    if "minute" in last_update:
        return "Data may be outdated. Click to Refresh."
    else:
        return pretty_date(shareData.last_update)