
from werkzeug.wrappers import Response

def application(environ, start_response):
    response = Response(u'Hello World', mimetype="text/html")
    return response(environ, start_response)


if __name__ == "__main__":
    pass

