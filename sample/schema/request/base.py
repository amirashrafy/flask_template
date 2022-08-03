from flask_restx import reqparse


base_parser = reqparse.RequestParser()
base_parser.add_argument('lang', location='args')
