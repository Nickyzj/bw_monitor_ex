from flask import Flask, Blueprint, render_template, url_for, redirect, flash
from flask import current_app as app
from control_panel.model import RFCItem
import control_panel.share_data as shareData
from utils.time_format import pretty_date

dashboard = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard.route('/')
def monitorDataList():
    last_update = pretty_date(shareData.last_update)
    return render_template('monitor_list.html', data = shareData.monitorData, last_update = last_update)

@dashboard.route('/<log_id>/<variante>')
def monitorDataDetail(log_id, variante):
    item = findByIDAndVar(log_id, variante)
    app.logger.info(item)
    return render_template('monitor_detail.html', data = item)

@dashboard.route('/rfc_call/<rfc_type>/<log_id>/<variante>')
def rfcCallChar(rfc_type, log_id, variante):
    if shareData.rfcCall.status == 'ready':
        result = findByIDAndVar(log_id, variante)
        if result:
            rfcItem =  RFCItem(result)
        else:
            flash('Please refresh data.')
        if rfc_type == 'char':
            rfcItem.rfcName = 'ZCHAIN_REMOVE_INVALID_CHAR'
        elif rfc_type == 'activate':
            rfcItem.rfcName = 'ZCHAIN_ACTIVATE_TR_DTP'
        elif rfc_type == 'repeat':
            rfcItem.rfcName = 'ZCHAIN_STEP_REPEAT'
        elif rfc_type == 'ignore':
            rfcItem.rfcName = 'ZCHAIN_IGNORE_VARIANT'

        shareData.rfcCall.setRFCCall(rfcItem.serialize())
        flash('RFC Call ' + rfcItem.rfcName + ' is executing.')
    else:
        flash('RFC call in process. Please try again later.')
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
    return pretty_date(shareData.last_update)