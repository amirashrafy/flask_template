from sample.util import int_number
from .base import base_parser


sample_parser = base_parser.copy()
sample_parser.add_argument('text', type=int_number, location='args')
