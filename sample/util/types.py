from . import BadRequest, ValueIsNotIntNumber
from flask import escape


def req_int_number(value):
    try:
        int(value)
    except Exception:
        raise_error(ValueIsNotIntNumber)
    return int(value)


def int_number(value):
    if len(value) == 0:
        return None
    return req_int_number(value)


def req_string(value):
    if len(value) == 0:
        raise_error(BadRequest)
    return value


def string(value):
    if len(value) == 0:
        return None
    return req_string(value)


def req_text(value):
    if len(value) == 0:
        raise_error(BadRequest)
    return str(escape(value))


def text(value):
    if len(value) == 0:
        return None
    return str(escape(req_string(value)))


def raise_error(error):
    try:
        exception_class_name = error.__name__
    except Exception:
        exception_class_name = BadRequest.__name__
    raise ValueError(exception_class_name)
