import time

from flask import Blueprint, request, jsonify, flash, render_template, current_app
import json
import datetime
import control_panel.share_data as shareData

data = Blueprint('data', __name__, template_folder='templates')

@data.route('/test')
def test():
    return 'api test page'

@data.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return 'upload'
    elif request.method == 'POST':
        content = request.json
        shareData.monitorData = json.loads(content)
        shareData.last_update = datetime.datetime.now()
        return 'success'


@data.route('/execute')
def execute():
    if shareData.rfcCall.sendMsg:
        sendMessage = shareData.rfcCall.executeRFCCall()
        return jsonify(sendMessage)
    else:
        return jsonify({})

@data.route('/execute/status', methods=['POST'])
def getStatus():
    content = request.json
    print(content)
    shareData.rfcCall.executeRFCCallComplete(content)
    return 'success'

@data.route('/execute/ajax_update')
def ajaxUpdate():
    while shareData.rfcCall.status != 'ready':
        time.sleep(1)
    flash(str(shareData.rfcCall.returnMsg))
    return render_template('flash_message.html')