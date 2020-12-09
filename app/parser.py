from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

class PlainTextParser():
    """
    Plain text parser.
    """
    media_type = 'text/plain'

    def parse(stream, media_type=None, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        return stream.read()