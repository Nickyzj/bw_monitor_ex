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
            ,'BATCHTIME = {0.BATCHTIME}\n' \
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
        return {
            'rfcName': self.rfcName,
            'CHAIN_AUTO_FIX' : self.CHAIN_AUTO_FIX,
            'LOG_ID' : self.LOG_ID,
            'CHAIN_ID' : self.CHAIN_ID,
            'CHAIN_TEXT' : self.CHAIN_TEXT,
            'TYPE' : self.TYPE,
            'VARIANTE' : self.VARIANTE,
            'VARIANTE_TEXT' : self.VARIANTE_TEXT,
            'INSTANCE' : self.INSTANCE,
            'JOB_COUNT' : self.JOB_COUNT,
            'ACTUAL_STATE' : self.ACTUAL_STATE,
            'ACTIVE_TIME' : self.ACTIVE_TIME,
            'BATCHDATE' : self.BATCHDATE,
            'BATCHTIME' : self.BATCHTIME,
            'SUGGEST_ACTION' : self.SUGGEST_ACTION,
            'FAILED_TIMES' : self.FAILED_TIMES,
            'LAST_FIX_DATE' : self.LAST_FIX_DATE,
            'LAST_FIX_TIME' : self.LAST_FIX_TIME,
            'LAST_FIX_ACTION' : self.LAST_FIX_ACTION,
            'ERROR_KEY_WORD' : self.ERROR_KEY_WORD
        }

class MonitorData:

    def __init__(self, rfcItem):
        self.id = rfcItem.LOG_ID + rfcItem.VARIANTE
        self.status = 0
        self.rfcItem = rfcItem

    def __repr__(self):
        return 'MonitorData({0.id!r}, {0.status!r})\n'.format(self)

    def __str(self):
        return '({0.id!r}, {0.status!r})\n'.format(self)

