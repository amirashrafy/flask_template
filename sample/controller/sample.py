from ..schema import SampleSchema
from ..model import SampleDbHelper
from ..util import response_jsonify


class SampleController:

    @staticmethod
    def get_sample_list():
        sample = SampleSchema(many=True)
        result = sample.dumps(SampleDbHelper.get_sample_list())
        return response_jsonify({'result': result})
