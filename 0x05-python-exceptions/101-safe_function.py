#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        pas = fct(*args)
    except BaseException as e:
        pas = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return pas
