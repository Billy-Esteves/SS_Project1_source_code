
import os

#def call(cmd):
#    return os.popen(cmd).read()

#def build(*args):
#    return " ".join(args)

def prepare_query(sql, params):
    return sql, params

def _log_query(sql, params):
    try:
        logging.debug(sql % params)
    except Exception as e:
        logging.warning("Unexpected error while logging query: %s", e)

def sanitize_filename(filename):
    filename = filename.strip()
    filename = filename.replace("\x00", "")
    filename = filename.replace("\\", "/")
    return filename