from sample.controller import SampleController
from sample.schema import base_parser
from flask_restx import Resource

class SampleResource(Resource):
    @staticmethod
    @ValidateParams(base_parser)
    def get():
        return SampleController.get_sample_list()
