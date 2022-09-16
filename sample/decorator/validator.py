from functools import wraps
from flask import g
from sample.app import api_v1 as api
from ..schema.request import base_parser
from ..util import BadRequest, p


class ValidateParams(object):
    def __init__(self, schema=None):
        self.schema = schema if schema is not None else base_parser

    def __call__(self, f):
        decorator_self = self

        @wraps(f)
        @api.doc(params=self.export_params(self.schema))
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


    @staticmethod
    def export_params(schema):
        params = {}
        properties = {}
        for arg in schema.args:
            if 'headers' in arg.location:
                in_location = 'header'
            elif 'json' in arg.location:
                in_location = 'body'
            elif 'args' in arg.location:
                in_location = 'query'
            else:
                in_location = 'body'

            if arg.type.__name__ == 'number' or arg.type.__name__ == 'req_number':
                param_type = 'number'
            elif arg.type.__name__ == 'string' or arg.type.__name__ == 'req_string' or arg.type.__name__ == 'text':
                param_type = 'string'
            elif arg.type.__name__ == 'boolean':
                param_type = 'boolean'
            else:
                param_type = 'string'
            if 'json' not in arg.location:
                temp = {'in': in_location, 'type': param_type, 'required': arg.required, 'description': arg.help}
                params[arg.name] = temp
            else:

                properties[arg.name] = {'type': param_type, 'description': arg.help, 'required': arg.required}
        if bool(properties):
            params['json'] = {'required': True, 'in': 'body', 'type': 'object', 'schema': {"type": "object", 'properties': properties}}
        return params
