import datetime

monitorData = []
last_update = datetime.datetime.now()

class RFCCall:

    def __init__(self):
        self.sendMsg = ''
        self.returnMsg = ''
        self.status = 'ready'

    def setRFCCall(self, sendMsg):
        self.sendMsg = sendMsg
        self.status = 'waiting'

    def executeRFCCall(self):
        self.status = 'executing'
        sendMessage = self.sendMsg
        self.sendMsg = None
        return sendMessage

    def executeRFCCallComplete(self, returnMsg):
        self.returnMsg = returnMsg
        self.status = 'ready'

rfcCall = RFCCall()