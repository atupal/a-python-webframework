
from paste.response import HeaderDict
from paste.response import parse_formvars

class Request(object):
    def __init__(self, environ):
        self.environ = environ
        self.fields = parse_formvars(environ)

    def Response(object):
        def __init__(self):
            self.headers = HeaderDict({
                "content-type": "text/html"
                })

