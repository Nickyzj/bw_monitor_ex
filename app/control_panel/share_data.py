import datetime, time, threading

monitorData = []
# last_update = datetime.datetime.now()
last_update = None

rfcCallName = {
    "fix char": "ZCHAIN_REMOVE_INVALID_CHAR",
    "activate": "ZCHAIN_ACTIVATE_TR_DTP",
    "repeat": "ZCHAIN_STEP_REPEAT",
    "ignore": "ZCHAIN_IGNORE_VARIANT",
    "skip": "ZCHAIN_SKIP_STEP",
}

rfcCallDesc = {
    "fix char": "Remove invalid text from DSO New table.",
    "activate": "Activate transformation and DTP.",
    "repeat": "Repeat this step.",
    "ignore": "Hide the variant from the list.",
    "skip": "Skip this step in process chain.",
}

class RFCCall:

    def __init__(self):
        self.sendMsg = ''
        self.returnMsg = ''
        self.status = 'ready'

    def setRFCCall(self, sendMsg):
        self.sendMsg = sendMsg
        self.status = 'waiting'
        t = threading.Thread(target=self.setTimeout, args=())
        t.start()

    def executeRFCCall(self):
        self.status = 'executing'
        sendMessage = self.sendMsg
        self.sendMsg = None
        return sendMessage

    def executeRFCCallComplete(self, returnMsg):
        self.returnMsg = returnMsg
        self.status = 'ready'

    def timeoutRFCCall(self):
        self.sendMsg = ''
        self.returnMsg = '{"error": "Timeout"}'
        self.status = 'ready'

    def setTimeout(self, sec = 60):
        start = datetime.datetime.now()
        print(start)
        while self.status != 'ready':
            diff = datetime.datetime.now() - start
            if diff.seconds > sec:
                print('Timeout {} seconds.'.format(sec))
                self.timeoutRFCCall()
                return
            else:
                time.sleep(1)

rfcCall = RFCCall()
