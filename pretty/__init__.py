#!/usr/bin/env python3
from __future__ import print_function
import logging
import inspect
import pandas as pd
import datetime
import os
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(
        format= '%(asctime)s %(levelname)s %(message)s',
        datefmt='%y-%m-%d %H:%M:%S')


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def critical(msg):
    logger.critical(msg)

def info(msg):
    logger.info(msg)

def debug(msg):
    logger.debug(msg)

def pretty_debug(func):
    def wrap(*args):
        sig = inspect.signature(func)
        function_file = os.path.basename(inspect.getfile(func))
        logger.debug(f'{function_file} {func.__name__}{sig}')
        for name, value in dict(zip(sig.parameters.items(), args)).items():
            if isinstance(value, pd.DataFrame) or isinstance(value, pd.Series):
                eprint(f'  ---> {name[0]}:')
                eprint(f'{value}')
            else:
                eprint(f'  ---> {name[0]} = {value}')
        start = datetime.datetime.now()
        f = func(*args)
        end = datetime.datetime.now()
        total = end - start
        total = total.microseconds
        eprint(f'  {func.__name__} took: {total} microseconds')
        return f
    return wrap
