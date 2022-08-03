from os import environ
from dotenv import load_dotenv

load_dotenv()


class Config:
    # ============================== Global Configuration ================================
    APP_NAME = environ.get('APP_NAME', "sample")
    ENV = environ.get("USER_ENV", "production")
    DEBUG = int(environ.get("TICKET_DEBUG", "0"))
    TIMEZONE = environ.get("TICKET_TIMEZONE", "Asia/Tehran")
    DATE_TIME_FORMAT = environ.get("DATE_TIME_FORMAT", "%Y-%m-%dT%H:%M:%S.000Z")
    VERIFICATION_CODE_LENGTH = environ.get("VERIFICATION_CODE_LENGTH", "6")
    SWAGGER_ENABLE = bool(environ.get("SWAGGER_ENABLE", False))
    # ============================= Postgres Configuration ==============================
    SQLALCHEMY_DATABASE_URI = environ.get("POSTGRES_URL", None)
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_RECORD_QUERIES = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
    # ============================= flask Configuration ================================
    TRAP_HTTP_EXCEPTIONS = bool(environ.get("TRAP_HTTP_EXCEPTIONS", True))
    PROPAGATE_EXCEPTIONS = bool(environ.get("PROPAGATE_EXCEPTIONS", True))



