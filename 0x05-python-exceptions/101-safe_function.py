#!/usr/bin/python3
def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as exc:
        print("Exception:", exc)
    return result
