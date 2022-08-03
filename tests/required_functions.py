from sample.app import db


def createParams(**kwargs):
    return kwargs


def reset_db(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
