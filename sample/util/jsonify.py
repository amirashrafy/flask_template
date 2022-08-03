from flask import current_app


def response_jsonify(state={}, metadata={}, status=200, headers={}):
    data = state
    data.update(metadata)
    data["status"] = True
    return data, status, headers
