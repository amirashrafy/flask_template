import sys
import traceback
from flask import request, jsonify
from ..util import p, Unknown


class ErrorHandling:

    @staticmethod
    def init_app(app):
        p("Init ErrorHandler")

        @app.errorhandler(Exception)
        def handle_invalid_usage(error):
            _, error_class, tb = sys.exc_info()

            error_tag = type(error_class).__name__ or 'Error On Name'
            error_file = str(traceback.extract_tb(tb)[-1]) or 'Error on file address'
            error_text = str(traceback.format_exc()) or 'Error on text error'
            p(error_tag)
            p(error_file)
            p(error_text)

            if request.args.get("lang") is None or \
                    len(request.args.get("lang")) or not \
                    (Unknown.message.__contains__(request.args.get("lang"))):
                lang = "fa"
            else:
                lang = request.args.get("lang")

            try:
                message = error.message[lang]
                status = error.status
            except:
                message = Unknown.message[lang]
                status = Unknown.status

            response = jsonify(
                status=False,
                msg=message
            )
            response.status_code = status
            return response
