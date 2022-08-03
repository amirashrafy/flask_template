from functools import wraps
from flask import g
from ..schema.request import base_parser
from ..util import BadRequest, p


class ValidateParams(object):
    def __init__(self, schema=None):
        self.schema = schema if schema is not None else base_parser

    def __call__(self, f):
        decorator_self = self

        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                g.params = self.schema.parse_args(strict=True)
            except Exception as e:
                if hasattr(e, 'data') and e.data.get('errors') is not None and len(e.data.get('errors').values()) > 0:
                    try:
                        exception_class = getattr(__import__('users.util.exceptions', fromlist=['UnknownError']),
                                                  list(e.data.get('errors').values())[0])
                    except Exception as e:
                        exception_class = getattr(__import__('users.util.exceptions', fromlist=['UnknownError']),
                                                  'BadRequest')
                        p(e)
                    raise exception_class
                else:
                    raise BadRequest

            return f(*args, **kwargs)

        return wrapper
