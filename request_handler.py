import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class HandleRequests(BaseHTTPRequestHandler):
  def parse_url(self, path):
      # Just like splitting a string in JavaScript. If the
      # path is "/animals/1", the resulting list will
      # have "" at index 0, "animals" at index 1, and "1"
      # at index 2.
      path_params = path.split("/")
      resource = path_params[1]
      id = None

      # Try to get the item at index 2
      try:
          # Convert the string "1" to the integer 1
          # This is the new parseInt()
          id = int(path_params[2])
      except IndexError:
          pass  # No route parameter exists: /animals
      except ValueError:
          pass  # Request had trailing slash: /animals/

      return (resource, id)  # This is a tuple

  def do_GET(self):
    self._set_headers(200)
    response = {}  # Default response

    # Parse the URL and capture the tuple that is returned
    (resource, id) = self.parse_url(self.path)

    if resource == "":
        if id is not None:
            response = {}
            if response is not None:
              self._set_headers(200)
              response = ''

            else:
              self._set_headers(404)
              response = {}
        else:
          self._set_headers(200)
          response = {}

    self.wfile.write(json.dumps(response).encode())