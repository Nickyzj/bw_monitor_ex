import requests
from redis import Redis
import rq
from threading import Thread

def send_to_redis(url):
    print('Task start...')
    queue = rq.Queue('my-tasks', connection=Redis.from_url('redis://'))
    job = queue.enqueue('rq_request.send_request', url)
    print(job.get_id())

def run_auto_fix(env):
    url = check_rules(env)
    if url:
        Thread(target=send_to_redis, args=(url,)).start()
    else:
        print("No auto fix job found.")

def check_rules(env):
    url = None
    for item in env.monitorList:
        if item.SUGGEST_ACTION == 'ACTIVATE_TR_DTP' and item.LAST_FIX_ACTION == '':
            print('ZCHAIN_ACTIVATE_TR_DTP')
            url = create_url('activate', item, env.name)
            break;
        if item.SUGGEST_ACTION == 'SKIP' and item.LAST_FIX_ACTION == '' and item.ACTUAL_STATE == 'R':
            print('ZCHAIN_SKIP_STEP')
            url = create_url('skip', item, env.name)
            break;
    return url
# def rules():
# '/rfc_call/<rfc_type>/<log_id>/<variante>/<env>'
bw_monitor_host = 'http://localhost:5000'

def create_url(rfc_type, item, env):
    url = '{}/monitor/rfc_call/{}/{}/{}/{}'.format(bw_monitor_host, rfc_type, item.LOG_ID, item.VARIANTE, env)
    print(url)
    return url
