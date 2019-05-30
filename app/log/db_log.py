import datetime
import sqlite3
from app.config import DATABASE
from app.utils.datetime_utils import get_tzlocal_now, convert_str_to_time, convert_str_to_date, convert_local_to_mst


def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def get_cursor(db):
    return db.cursor()

def write_db(query, args=()):
    db = None
    cursor = None
    try:
        db = get_db()
        cursor = get_cursor(db)
        cursor.execute(query, args)
        db.commit()
        return cursor.lastrowid
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

def set_rfc_call_query(env, rfcItem, status, remote_addr):
    query = """
        insert into rfc_call_history (
            ENVIRONMENT,
            CHAIN_AUTO_FIX,
            LOG_ID,
            CHAIN_ID,
            CHAIN_TEXT,
            TYPE,
            VARIANTE,
            VARIANTE_TEXT,
            INSTANCE,
            JOB_COUNT,
            ACTUAL_STATE,
            ACTIVE_TIME,
            BATCHDATE,
            BATCHTIME,
            SUGGEST_ACTION,
            FAILED_TIMES,
            FIX_DATE,
            FIX_TIME,
            FIX_ACTION,
            ERROR_KEY_WORD,
            STATUS,
            IP) values (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
    """

    args = (env,
            rfcItem.CHAIN_AUTO_FIX,
            rfcItem.LOG_ID,
            rfcItem.CHAIN_ID,
            rfcItem.CHAIN_TEXT,
            rfcItem.TYPE,
            rfcItem.VARIANTE,
            rfcItem.VARIANTE_TEXT,
            rfcItem.INSTANCE,
            rfcItem.JOB_COUNT,
            rfcItem.ACTUAL_STATE,
            rfcItem.ACTIVE_TIME,
            convert_str_to_date(rfcItem.BATCHDATE),
            convert_str_to_time(rfcItem.BATCHTIME),
            rfcItem.SUGGEST_ACTION,
            rfcItem.FAILED_TIMES_3_DAYS,
            convert_local_to_mst(get_tzlocal_now()).strftime("%Y-%m-%d"),
            convert_local_to_mst(get_tzlocal_now()).strftime("%H:%M:%S"),
            rfcItem.rfcName,
            rfcItem.ERROR_KEY_WORD,
            status,
            remote_addr
            )
    return query, args

def rfc_log_insert(env, rfcItem, status, remote_addr):
    query, args = set_rfc_call_query(env, rfcItem, status, remote_addr)
    return write_db(query, args)

def rfc_log_execute(lastrowid, status):
    query = "update rfc_call_history set status = ? where id = ?"
    write_db(query, (status, lastrowid))

def rfc_log_execute_complete(lastrowid, status, message):
    query = "update rfc_call_history set status = ?, RETURN_MSG = ? where id = ?"
    write_db(query, (status, str(message), lastrowid))

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def findAllLog():
    db = None
    cursor = None
    try:
        db = get_db()
        cursor = get_cursor(db)
        result = cursor.execute("select * from rfc_call_history order by id desc limit 10")
        return result.fetchall()
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

def findLogById(id):
    db = None
    cursor = None
    try:
        db = get_db()
        cursor = get_cursor(db)
        result = cursor.execute("select * from rfc_call_history where id = ?", (id,))
        return result.fetchone()
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

def init_db():
    db = None
    cursor = None
    try:
        db = get_db()
        cursor = get_cursor(db)
        with open('schema.sql') as fp:
            cursor.executescript(fp.read())
    except Exception as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()