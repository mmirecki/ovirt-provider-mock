from BaseHTTPServer import BaseHTTPRequestHandler
from neutron.responses import get_responses
from neutron.responses import post_responses


class TestConnectionHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET:  " + self.path)

        path = self.parse_request_path(self.path)
        response_key = self.parse_response_key(path)
        response = get_responses.get(response_key)
        if not response:
            self.send_response(400)
            self.wfile.write("Incorrect path")
            return

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("x-openstack-request-id",
                         "req-edf1f07f-1ccf-4d42-a073-b2bd99bb9f4a")

        self.end_headers()
        result = response.response(path)
        print("path: " + str(path))

        print("RESPONSE: " + str(response))

        self.wfile.write(result)

        return

    # this is a duplicate of do_GET
    # I'm not exctracting a comon function, because for now it is easier
    # to debug like this
    def do_POST(self):
        print("POST:  " + self.path)
        content_length = int(self.headers['Content-Length'])
        content = self.rfile.read(content_length)
        print("Body:")
        print(content)

        path = self.parse_request_path(self.path)
        response_key = self.parse_response_key(path)
        response = post_responses.get(response_key)
        if not response:
            print("No such response")
            self.send_response(400)
            self.wfile.write("Incorrect path")
            return

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("x-openstack-request-id",
                         "req-edf1f07f-1ccf-4d42-a073-b2bd99bb9f4a")

        self.end_headers()
        response_content = response.response(path, content)
        print("RESPONSE:")
        print(response_content)
        self.wfile.write(response_content)

        return

    def do_PUT(self):
        print("PUT:  " + self.path)

    def do_DELETE(self):
        print("DELETE:  " + self.path)
        self.send_header("x-openstack-request-id",
                         "req-edf1f07f-1ccf-4d42-a073-b2bd99bb9f4a")

        self.end_headers()

        path = self.parse_request_path(self.path)
        response_key = self.parse_response_key(path)
        response = get_responses.get(response_key)
        if not response:
            self.send_response(400)
            self.wfile.write("Incorrect path")
            return

        self.send_response(204)
        self.wfile.write(response.response(path))

        return

    """
    The request path looks like: "/v2.0/*" example: "/v2.0/networks".
    We are only interested in the * part
    """
    def parse_request_path(self, full_path):
        if len(full_path) < 6:
            return None
        return full_path[6:]

    def parse_response_key(self, path):
        slash_index = str.find(path, "/")
        if slash_index < 0:
            return path
        return path[:slash_index+1]
