from sample.app import api_v1 as api
from .sample import *

api.add_resource(
    SampleResource,
    "/sample",
    methods=['GET']
)
