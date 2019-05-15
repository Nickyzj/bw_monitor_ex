# from app.control_panel.model import RFCCall
from app.control_panel.model import Enviornment

# rfcCallName = {
#             "fix char": "ZCHAIN_REMOVE_INVALID_CHAR",
#             "activate": "ZCHAIN_ACTIVATE_TR_DTP",
#             "repeat": "ZCHAIN_STEP_REPEAT",
#             "ignore": "ZCHAIN_IGNORE_VARIANT",
#             "skip": "ZCHAIN_SKIP_STEP",
#         }
# rfcCallDesc = {
#             "fix char": "Remove invalid text from DSO New table.",
#             "activate": "Activate transformation and DTP.",
#             "repeat": "Repeat this step.",
#             "ignore": "Hide the variant from the list.",
#             "skip": "Skip this step in process chain.",
#         }
#
# rfcCall = RFCCall()
#
# monitorData = []
# last_update = None

# qcb = Enviornment('qcb')
# pcb = Enviornment('pcb')
environments = {}
environments['qcb'] = Enviornment('qcb')
environments['pcb'] = Enviornment('pcb')
