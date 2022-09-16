from flask import Flask, Blueprint
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from .config import Config
from .util import ErrorHandling


db = SQLAlchemy()
ma = Marshmallow()
eh = ErrorHandling()
api_v1_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")
api_v1 = Api(api_v1_bp, doc=False) if not Config.SWAGGER_ENABLE else Api(api_v1_bp, doc="/doc")

import sample.resource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)
    eh.init_app(app)
    if not Config.SWAGGER_ENABLE:
        api_v1.init_app(app, add_specs=False)
    app.register_blueprint(api_v1_bp)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    return app
