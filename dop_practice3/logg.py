from pip._internal.utils import logging
from imports import *

first()

def f():
    try:
        1 / 0
    except Exception as ex:
        message = "An exception of type {0} occurred. Arguments:\n{1!r}"
        return message.format(type(ex).__name__, ex.args)

def run_with_log(func):
    log = logging.getLogger()
    log.exception(func())

run_with_log(f)
