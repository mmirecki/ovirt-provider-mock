from BaseHTTPServer import BaseHTTPRequestHandler
from neutron.responses import get_responses
from neutron.responses import show_responses
from neutron.responses import post_responses
from neutron.responses import delete_responses
from neutron.responses import put_responses
from neutron.responses import debug


class TestConnectionHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("\n\nGET:  " + self.path)

        path = self._parse_request_path(self.path)
        response_key = self._parse_response_key(self.path)
        if self._is_list(path):
            response = get_responses.get(response_key)
        else:
            response = show_responses.get(response_key)

        self._process_request(response)

    def do_POST(self):
        print("\n\nPOST:  " + self.path)
        content = self.get_content()
        print("Body:\n" + content)
        response_key = self._parse_response_key(self.path)
        response = post_responses.get(response_key)

        self._process_request(response, content=content)

    def do_PUT(self):
        print("\n\nPUT:  " + self.path)
        content = self.get_content()
        print("Body:\n" + content)

        response_key = self._parse_response_key(self.path)
        response = put_responses.get(response_key)

        self._process_request(response, content=content)

    def do_DELETE(self):
        print("\n\nDELETE:  " + self.path)

        response_key = self._parse_response_key(self.path)
        response = delete_responses.get(response_key)

        self._process_request(response, 204, False)

    def _process_request(self, response, response_code=200, send_response=True,
                         content=None):
        if not response:
            print("No such response")
            self.send_response(400)
            self.wfile.write("Incorrect path")
            return

        path = self._parse_request_path(self.path)

        self.send_response(response_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("x-openstack-request-id",
                         "req-edf1f07f-1ccf-4d42-a073-b2bd99bb9f4a")
        self.end_headers()

        try:
            if content:
                response_content = response.response(path, content)
            else:
                response_content = response.response(path)
        except BaseException as e:
            print("Error:\n" + str(e))
            self.send_response(500)
            self.wfile.write("Error:\n" + str(e))
            return

        if send_response:
            print("RESPONSE:")
            print(response_content)
        self.wfile.write(response_content)

    """
    The request path looks like: "/v2.0/*" example: "/v2.0/networks".
    We are only interested in the * part
    """
    def _parse_request_path(self, full_path):
        if len(full_path) < 6:
            return None
        return full_path[6:]

    def _parse_response_key(self, in_path):
        path = self._parse_request_path(self.path)

        slash_index = str.find(path, "/")
        if slash_index < 0:
            return path
        return path[:slash_index]

    def _is_list(self, full_path):
        slash_index = str.find(full_path, "/")
        return slash_index < 0

    def get_content(self):
        content_length = int(self.headers['Content-Length'])
        content = self.rfile.read(content_length)
        return content
