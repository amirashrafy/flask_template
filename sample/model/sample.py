from ..app import db
from ..util import now


class SampleModel(db.Model):
    __tablename__ = 'sample'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    created_at = db.Column(db.DateTime, default=now, nullable=False)


class SampleDbHelper:

    @staticmethod
    def get_sample_list():
        query = SampleModel.query
        return query.all()
