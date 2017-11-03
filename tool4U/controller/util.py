import re
import os
import sys
import copy
import datetime
import StringIO
import threading
import traceback
from json import dumps, loads
from config import envConfig


def catcher(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception, e:
            trace_file = StringIO.StringIO()
            trace_file.write(
                "\n\n[%s] Input Arguments: [%s].%s" % (
                    datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"),
                    repr((args, kwargs)), os.linesep
                )
            )
            trace_file.write("Catch Exception: [%s]%s" % (e.message, os.linesep))
            traceback.print_stack(file=trace_file)
            trace_file.seek(0)
            with open(envConfig.envConfigs['log'], 'a+') as _f:
                _f.write(trace_file.read())

            del trace_file
            logger(dumps({
                "responseCode": "9999",
                "responseMsg": e.message
            }, indent=4))

            sys.exit(-1)

    return wrapper

def logger(obj):
    if not isinstance(obj, str):
        obj = repr(obj)
    sys.stdout.write(obj.decode("unicode-escape") + os.linesep)
