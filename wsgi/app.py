
def application(eviron, start_response):
  response_body = 'Hello World'
  status=  '200 OK'

  resposne_header = [
      ('Content-Type', 'text/plain'),
      ('Content-Length', str(len(response_body)))
      ]

  start_response(status, resposne_header)

  return [response_body]
