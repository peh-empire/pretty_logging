#!/usr/bin/env python3
from __future__ import print_function
import logging
import inspect
import datetime
import os
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(
        format= '%(asctime)s %(levelname)s %(message)s',
        datefmt='%y-%m-%d %H:%M:%S')


def set_level(level):
    logger.setLevel(level)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def critical(msg):
    logger.critical(msg)

def info(msg):
    logger.info(msg)

def debug(msg):
    logger.debug(msg)


def timeit(func):
    def wrap(*args):
        start = datetime.datetime.now()
        f = func(*args)
        end = datetime.datetime.now()
        total = end - start
        
        eprint(f'  {func.__name__} took: {total}')
        return f
    return wrap


def pretty_debug(func):
    def wrap(*args):
        sig = inspect.signature(func)
        function_file = os.path.basename(inspect.getfile(func))
        logger.debug(f'{function_file} {func.__name__}{sig}')
        if logger.getEffectiveLevel() == logging.DEBUG:
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
        return func(*args)
    return wrap
