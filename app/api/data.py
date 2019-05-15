import time

from flask import Blueprint, request, jsonify, flash, render_template, current_app
import json
import datetime
from app.control_panel.share_data import environments

data = Blueprint('data', __name__, template_folder='templates')

@data.route('/test')
def test():
    return 'api test page'

@data.route('/upload/<env>', methods=['GET', 'POST'])
def upload(env):
    if request.method == 'GET':
        return 'upload'
    elif request.method == 'POST':
        content = request.json
        environments[env].monitorData = json.loads(content)
        environments[env].last_update = datetime.datetime.now()
        return 'success'


@data.route('/execute/<env>')
def execute(env):
    if environments[env].rfcCall.sendMsg:
        sendMessage = environments[env].rfcCall.executeRFCCall()
        return jsonify(sendMessage)
    else:
        return jsonify({})

@data.route('/execute/status/<env>', methods=['POST'])
def getStatus(env):
    content = request.json
    print(content)
    environments[env].rfcCall.executeRFCCallComplete(content)
    return 'success'

@data.route('/execute/ajax_update/<env>')
def ajaxUpdate(env):
    while environments[env].rfcCall.status != 'ready':
        time.sleep(1)
    flash(str(environments[env].rfcCall.returnMsg), 'success')
    return render_template('flash_message.html')