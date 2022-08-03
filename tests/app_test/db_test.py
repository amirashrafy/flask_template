from sample.app import db


def test_database_connection(app):
    with app.app_context():
        result = db.engine.execute("SELECT current_database();").first()
        assert result[0] == "testing"
