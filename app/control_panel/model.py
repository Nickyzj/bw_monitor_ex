import datetime, time, threading
from app.log.db_log import rfc_log_insert, rfc_log_execute, rfc_log_execute_complete

class RFCItem:

    def __init__(self, item):
        self.rfcName = ''
        self.CHAIN_AUTO_FIX = item['CHAIN_AUTO_FIX']
        self.LOG_ID = item['LOG_ID']
        self.CHAIN_ID = item['CHAIN_ID']
        self.CHAIN_TEXT = item['CHAIN_TEXT']
        self.TYPE = item['TYPE']
        self.VARIANTE = item['VARIANTE']
        self.VARIANTE_TEXT = item['VARIANTE_TEXT']
        self.INSTANCE = item['INSTANCE']
        self.JOB_COUNT = item['JOB_COUNT']
        self.ACTUAL_STATE = item['ACTUAL_STATE']
        self.ACTIVE_TIME = item['ACTIVE_TIME']
        self.BATCHDATE = item['BATCHDATE']
        self.BATCHTIME = item['BATCHTIME']
        self.SUGGEST_ACTION = item['SUGGEST_ACTION']
        self.FAILED_TIMES = item['FAILED_TIMES']
        self.LAST_FIX_DATE = item['LAST_FIX_DATE']
        self.LAST_FIX_TIME = item['LAST_FIX_TIME']
        self.LAST_FIX_ACTION = item['LAST_FIX_ACTION']
        self.ERROR_KEY_WORD = item['ERROR_KEY_WORD']

    def __repr__(self):
        return 'RFC item:\n' \
               'CHAIN_AUTO_FIX = {0.CHAIN_AUTO_FIX}\n' \
               'LOG_ID = {0.LOG_ID}\n' \
               'CHAIN_ID = {0.CHAIN_ID}\n' \
               'CHAIN_TEXT = {0.CHAIN_TEXT}\n' \
               'TYPE = {0.TYPE}\n' \
               'VARIANTE = {0.VARIANTE}\n' \
               'VARIANTE_TEXT = {0.VARIANTE_TEXT}\n' \
               'INSTANCE = {0.INSTANCE}\n' \
               'JOB_COUNT = {0.JOB_COUNT}\n' \
               'ACTUAL_STATE = {0.ACTUAL_STATE}\n' \
               'ACTIVE_TIME = {0.ACTIVE_TIME}\n' \
               'BATCHDATE = {0.BATCHDATE}\n' \
            , 'BATCHTIME = {0.BATCHTIME}\n' \
              'SUGGEST_ACTION = {0.SUGGEST_ACTION}\n' \
              'FAILED_TIMES = {0.FAILED_TIMES}\n' \
              'LAST_FIX_DATE = {0.LAST_FIX_DATE}\n' \
              'LAST_FIX_TIME = {0.LAST_FIX_TIME}\n' \
              'LAST_FIX_ACTION = {0.LAST_FIX_ACTION}\n' \
              'ERROR_KEY_WORD = {0.ERROR_KEY_WORD}\n'.format(self)

    def __str__(self):
        return 'RFC item:\n' \
               'CHAIN_AUTO_FIX = {0.CHAIN_AUTO_FIX}\n' \
               'LOG_ID = {0.LOG_ID}\n' \
               'CHAIN_ID = {0.CHAIN_ID}\n' \
               'CHAIN_TEXT = {0.CHAIN_TEXT}\n' \
               'TYPE = {0.TYPE}\n' \
               'VARIANTE = {0.VARIANTE}\n' \
               'VARIANTE_TEXT = {0.VARIANTE_TEXT}\n' \
               'INSTANCE = {0.INSTANCE}\n' \
               'JOB_COUNT = {0.JOB_COUNT}\n' \
               'ACTUAL_STATE = {0.ACTUAL_STATE}\n' \
               'ACTIVE_TIME = {0.ACTIVE_TIME}\n' \
               'BATCHDATE = {0.BATCHDATE}\n' \
               'BATCHTIME = {0.BATCHTIME}\n' \
               'SUGGEST_ACTION = {0.SUGGEST_ACTION}\n' \
               'FAILED_TIMES = {0.FAILED_TIMES}\n' \
               'LAST_FIX_DATE = {0.LAST_FIX_DATE}\n' \
               'LAST_FIX_TIME = {0.LAST_FIX_TIME}\n' \
               'LAST_FIX_ACTION = {0.LAST_FIX_ACTION}\n' \
               'ERROR_KEY_WORD = {0.ERROR_KEY_WORD}\n'.format(self)

    def serialize(self):
        json_str = None
        try:
            json_str = {
                'rfcName': self.rfcName,
                'CHAIN_AUTO_FIX': self.CHAIN_AUTO_FIX,
                'LOG_ID': self.LOG_ID,
                'CHAIN_ID': self.CHAIN_ID,
                'CHAIN_TEXT': self.CHAIN_TEXT,
                'TYPE': self.TYPE,
                'VARIANTE': self.VARIANTE,
                'VARIANTE_TEXT': self.VARIANTE_TEXT,
                'INSTANCE': self.INSTANCE,
                'JOB_COUNT': self.JOB_COUNT,
                'ACTUAL_STATE': self.ACTUAL_STATE,
                'ACTIVE_TIME': self.ACTIVE_TIME,
                'BATCHDATE': self.BATCHDATE,
                'BATCHTIME': self.BATCHTIME,
                'SUGGEST_ACTION': self.SUGGEST_ACTION,
                'FAILED_TIMES': self.FAILED_TIMES,
                'LAST_FIX_DATE': self.LAST_FIX_DATE,
                'LAST_FIX_TIME': self.LAST_FIX_TIME,
                'LAST_FIX_ACTION': self.LAST_FIX_ACTION,
                'ERROR_KEY_WORD': self.ERROR_KEY_WORD
            }
        except KeyError as e:
            print(e)
        return json_str

class MonitorData:

    def __init__(self, rfcItem):
        self.id = rfcItem.LOG_ID + rfcItem.VARIANTE
        self.status = 0
        self.rfcItem = rfcItem

    def __repr__(self):
        return 'MonitorData({0.id!r}, {0.status!r})\n'.format(self)

    def __str(self):
        return '({0.id!r}, {0.status!r})\n'.format(self)


class RFCCall:

    def __init__(self):
        self.sendMsg = ''
        self.returnMsg = ''
        self.status = 'ready'
        self.rfcItem = None
        self.env = ''
        self.remote_addr = ''
        self.lastrowid = 0

    def setRFCCall(self, sendMsg):
        self.sendMsg = sendMsg
        self.status = 'waiting'
        self.lastrowid = rfc_log_insert(self.env, self.rfcItem, self.status, self.remote_addr)
        t = threading.Thread(target=self.setTimeout, args=())
        t.start()

    def executeRFCCall(self):
        self.status = 'executing'
        sendMessage = self.sendMsg
        self.sendMsg = None
        rfc_log_execute(self.lastrowid, self.status)
        return sendMessage

    def executeRFCCallComplete(self, returnMsg):
        self.returnMsg = returnMsg
        self.status = 'ready'
        rfc_log_execute_complete(self.lastrowid, 'completed', returnMsg)

    def timeoutRFCCall(self):
        self.sendMsg = ''
        self.returnMsg = '{"error": "Timeout"}'
        self.status = 'ready'

    def setTimeout(self, sec=60):
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



class Enviornment:

    def __init__(self, name):
        self.name = name
        self.monitorData = []
        self.last_update = None
        self.rfcCallName = {
            "fix char": "ZCHAIN_REMOVE_INVALID_CHAR",
            "activate": "ZCHAIN_ACTIVATE_TR_DTP",
            "repeat": "ZCHAIN_STEP_REPEAT",
            "ignore": "ZCHAIN_IGNORE_VARIANT",
            "skip": "ZCHAIN_SKIP_STEP",
        }
        self.rfcCallDesc = {
            "fix char": "Remove invalid text from DSO New table.",
            "activate": "Activate transformation and DTP.",
            "repeat": "Repeat this step.",
            "ignore": "Hide the variant from the list.",
            "skip": "Skip this step in process chain.",
        }
        self.rfcCall = RFCCall()
