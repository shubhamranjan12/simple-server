from wsgiref.simple_server import make_server
from wsgiref import util


def first():
    return [b'Hello from first!']

def second():
    return [b'Hello from Second!']

URLS = {'/first': [ first,'GET'], '/second': [second, 'GET']}

home = """<html>
  <title> Hello User </title>
  <body>
      <p> Please try these urls
          <ol>
             <li> /first </li>
             <li> /second </li>
          </ol>
      </p> 
  </body>
</html>
"""

def application(environ, start_response):
    if environ['PATH_INFO'] in URLS:
        start_response("200 OK", [("Content-type", "text/plain")])
        return URLS[environ['PATH_INFO']][0]()
    start_response("200 OK", [("Content-type", "text/html")])
    return [home.encode()]

server = make_server('0.0.0.0', 8080, application)
server.serve_forever()
