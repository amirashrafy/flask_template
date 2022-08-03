from sample.app import ma
from sample.config import Config
from sample.model.sample import SampleModel
from sample.schema.response import BaseSchema


class SampleSchema(BaseSchema):
    class Meta:
        model = SampleModel
        datetimeformat = Config.DATE_TIME_FORMAT

    id = ma.auto_field(dump_only=True)
    created_at = ma.auto_field(dump_only=True)
