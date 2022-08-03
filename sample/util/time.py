from datetime import datetime
from pytz import timezone, utc
from ..config import Config


def now(name=Config.TIMEZONE):
    tz = timezone(name)
    return datetime.utcnow().replace(tzinfo=utc).astimezone(tz).replace(microsecond=0, tzinfo=None)


def time_diff(from_date, to_date=''):
    to_date = to_date if isinstance(from_date, datetime) else datetime.now()
    from_date = from_date if isinstance(from_date, datetime) else datetime.fromisoformat(from_date)
    diff = to_date - from_date
    return diff.total_seconds()
