
from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

html = """
<html>
  <form method="get" action="parsing_get.wsgi">
  <p>
    Age: <input type="text" name="age">
  </p>

  <p>
    Hobbies:
    <input name="hobbies" type="checkbox" value="software"> Software
    <input name="hobbies" type="checkbox" value="tunning"> Auto Tunning
  </p>

  <p>
    <input type="submit" value="Submit">
  </p>
  </form>
  <p>
    Age: %s<br>
    Hobbies: %s
  </p>
</html>
"""

def app(environ, start_response):
  # Return a dictionary containing lists as value.
  d = parse_qs(environ['QUERY_STRING'])

  age = d.get('age', [''])[0]  # Returns the first age value.
  hobbies = d.get('hobbies', [])  # Returns a list of hobbies.

  response_body = html % (age or 'Empty', 
              ','.join(hobbies or ['No Hobbies']))

  status = '200 OK'

  # Now content type is text/html
  response_headers = [('Content-Type', 'text/html'),
                      ('Content-Length', str(len(html)))]

  start_response(status, response_headers)

  return [response_body]

httpd = make_server(
    '0.0.0.0',
    8888,
    app,
    )
 
#httpd.handle_request()   # just handle the reqeust once 
httpd.serve_forever()
