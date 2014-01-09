
from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

html = """
<html>
  <body>
    <form method="post" action="parsing_post.wsgi">
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
  </body>
</html>
"""

def app(environ, start_response):
  try:
    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
  except:
    request_body_size = 0


  # When the method is POST, the query string will be sent
  # in the HTTP request body which is passed by the WSGI server
  # in the file like wsgi.input environment variable.
  request_body = environ['wsgi.input'].read(request_body_size)
  d = parse_qs(request_body)

  age = d.get('age', [''])[0]
  hobbies = d.get('hobbies', [])

  age = escape(age)
  hobbies = [escape(hobby) for hobby in hobbies]

  response_body = html % (age or 'Empty', ','.join(hobbies or ['No Hobbies']))

  status = '200 OK'

  response_headers = [('Content-Type', 'text/html'),
                      ('Content-Length', str(len(response_body)))]

  start_response(status, response_headers)

  return [response_body]


httpd = make_server('0.0.0.0', 8888, app)
httpd.serve_forever()
