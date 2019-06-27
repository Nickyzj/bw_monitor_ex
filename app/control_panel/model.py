import datetime, time, threading
import pytz
from app.log.db_log import rfc_log_insert, rfc_log_execute, rfc_log_execute_complete


class RFCItem:

    def __init__(self, item):
        self.rfcName = ''
        self.CHAIN_AUTO_FIX = item.get('CHAIN_AUTO_FIX')
        self.LOG_ID = item.get('LOG_ID')
        self.CHAIN_ID = item.get('CHAIN_ID')
        self.CHAIN_TEXT = item.get('CHAIN_TEXT')
        self.TYPE = item.get('TYPE')
        self.VARIANTE = item.get('VARIANTE')
        self.VARIANTE_TEXT = item.get('VARIANTE_TEXT')
        self.INSTANCE = item.get('INSTANCE')
        self.JOB_COUNT = item.get('JOB_COUNT')
        self.ACTUAL_STATE = item.get('ACTUAL_STATE')
        self.ACTIVE_TIME = item.get('ACTIVE_TIME')
        self.BATCHDATE = item.get('BATCHDATE')
        self.BATCHTIME = item.get('BATCHTIME')
        self.SUGGEST_ACTION = item.get('SUGGEST_ACTION')
        self.FAILED_TIMES_3_DAYS = item.get('FAILED_TIMES_3_DAYS')
        self.LAST_FIX_DATE = item.get('LAST_FIX_DATE')
        self.LAST_FIX_TIME = item.get('LAST_FIX_TIME')
        self.LAST_FIX_ACTION = item.get('LAST_FIX_ACTION')
        self.ERROR_KEY_WORD = item.get('ERROR_KEY_WORD')
        self.LAST_SUCC_LOG_DATE = item.get('LAST_SUCC_LOG_DATE')
        self.LAST_SUCC_LOG_TIME = item.get('LAST_SUCC_LOG_TIME')
        self.NO_OF_LOGS_IN_3_DAYS = item.get('NO_OF_LOGS_IN_3_DAYS')
        self.RECENT_FAILED_LOGS_IN_3_DAYS = item.get('RECENT_FAILED_LOGS_IN_3_DAYS')
        self.TIMESTAMP_OF_LAST_SUCC_LOG = item.get('TIMESTAMP_OF_LAST_SUCC_LOG')
        self.batch_date_time_display = self.date_time_formatter_phx(self.BATCHDATE, self.BATCHTIME)
        if self.TIMESTAMP_OF_LAST_SUCC_LOG is None or self.TIMESTAMP_OF_LAST_SUCC_LOG == '':
            self.timestamp_of_last_succ_log_format = None
        else:
            self.timestamp_of_last_succ_log_format = datetime.datetime.strptime(
                self.TIMESTAMP_OF_LAST_SUCC_LOG,
                "%Y%m%d%H%M%S"
            )
        self.warning = ''
        self.set_warning()

    def set_warning(self):
        table_style = 'table-danger'
        if self.timestamp_of_last_succ_log_format is not None:
            utc_now = datetime.datetime.utcnow()
            time_diff = utc_now - self.timestamp_of_last_succ_log_format
            if time_diff >= datetime.timedelta(hours=6):
                self.warning = table_style
        if self.RECENT_FAILED_LOGS_IN_3_DAYS is not None and self.RECENT_FAILED_LOGS_IN_3_DAYS >= 2:
            self.warning = table_style

    def date_time_formatter_phx(self, date, time):
        datetime_object = datetime.datetime.strptime(str(date) + str(time), '%Y%m%d%H%M%S')
        mst = pytz.timezone('America/Phoenix')
        datetime_object = mst.localize(datetime_object)
        return datetime_object

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
               'BATCHTIME = {0.BATCHTIME}\n' \
               'SUGGEST_ACTION = {0.SUGGEST_ACTION}\n' \
               'FAILED_TIMES_3_DAYS = {0.FAILED_TIMES_3_DAYS}\n' \
               'LAST_FIX_DATE = {0.LAST_FIX_DATE}\n' \
               'LAST_FIX_TIME = {0.LAST_FIX_TIME}\n' \
               'LAST_FIX_ACTION = {0.LAST_FIX_ACTION}\n' \
               'ERROR_KEY_WORD = {0.ERROR_KEY_WORD}\n' \
               'LAST_SUCC_LOG_DATE = {0.LAST_SUCC_LOG_DATE}\n' \
               'LAST_SUCC_LOG_TIME = {0.LAST_SUCC_LOG_TIME}\n' \
               'NO_OF_LOGS_IN_3_DAYS = {0.NO_OF_LOGS_IN_3_DAYS}\n' \
               'RECENT_FAILED_LOGS_IN_3_DAYS = {0.RECENT_FAILED_LOGS_IN_3_DAYS}\n' \
               'TIMESTAMP_OF_LAST_SUCC_LOG = {0.TIMESTAMP_OF_LAST_SUCC_LOG}\n' \
            .format(self)

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
               'FAILED_TIMES_3_DAYS = {0.FAILED_TIMES_3_DAYS}\n' \
               'LAST_FIX_DATE = {0.LAST_FIX_DATE}\n' \
               'LAST_FIX_TIME = {0.LAST_FIX_TIME}\n' \
               'LAST_FIX_ACTION = {0.LAST_FIX_ACTION}\n' \
               'ERROR_KEY_WORD = {0.ERROR_KEY_WORD}\n' \
               'LAST_SUCC_LOG_DATE = {0.LAST_SUCC_LOG_DATE}\n' \
               'LAST_SUCC_LOG_TIME = {0.LAST_SUCC_LOG_TIME}\n' \
               'NO_OF_LOGS_IN_3_DAYS = {0.NO_OF_LOGS_IN_3_DAYS}\n' \
               'RECENT_FAILED_LOGS_IN_3_DAYS = {0.RECENT_FAILED_LOGS_IN_3_DAYS}\n' \
               'TIMESTAMP_OF_LAST_SUCC_LOG = {0.TIMESTAMP_OF_LAST_SUCC_LOG}\n' \
            .format(self)

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
                'FAILED_TIMES_3_DAYS': self.FAILED_TIMES_3_DAYS,
                'LAST_FIX_DATE': self.LAST_FIX_DATE,
                'LAST_FIX_TIME': self.LAST_FIX_TIME,
                'LAST_FIX_ACTION': self.LAST_FIX_ACTION,
                'ERROR_KEY_WORD': self.ERROR_KEY_WORD,
                'LAST_SUCC_LOG_DATE': self.LAST_SUCC_LOG_DATE,
                'LAST_SUCC_LOG_TIME': self.LAST_SUCC_LOG_TIME,
                'NO_OF_LOGS_IN_3_DAYS': self.NO_OF_LOGS_IN_3_DAYS,
                'RECENT_FAILED_LOGS_IN_3_DAYS': self.RECENT_FAILED_LOGS_IN_3_DAYS,
                'TIMESTAMP_OF_LAST_SUCC_LOG': self.TIMESTAMP_OF_LAST_SUCC_LOG
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

    def setTimeout(self, sec=120):
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
        self.monitorList = []
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

    def init_monitor_list(self, data_list=None):
        if not data_list:
            data_list = self.monitorData
        self.monitorList = []
        for data in data_list:
            rfcItem = RFCItem(data)
            self.monitorList.append(rfcItem)
