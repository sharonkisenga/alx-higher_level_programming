#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        attente = a / b
    except ZeroDivisionError:
        attente = None
    finally:
        print("Inside attente: {}".format(attente))
        return attente
