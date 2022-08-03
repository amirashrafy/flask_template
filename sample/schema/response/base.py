import pytz
from marshmallow import pre_dump
from sample.app import ma
from sample.config import Config


class BaseSchema(ma.SQLAlchemySchema):

    @pre_dump()
    def changeTimeZone(self, data, **kwargs):
        keys = ['create_at', 'update_at', 'created_at', 'updated_at']
        old_timezone = pytz.timezone(Config.TIMEZONE)
        new_timezone = pytz.timezone("Etc/UTC")
        for key in keys:
            try:
                attr = data.__getattribute__(key)
                new_timezone_timestamp = old_timezone.localize(attr).astimezone(new_timezone)
                data.__setattr__(key, new_timezone_timestamp)
            except Exception:
                pass
        return data