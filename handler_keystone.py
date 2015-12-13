from BaseHTTPServer import BaseHTTPRequestHandler

class GetTokenHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "Application/json")
#        self.send_header("x-openstack-request-id", "req-edf1f07f-1ccf-4d42-a073-b2bd99bb9f4a")

        self.end_headers()
        self.wfile.write(self.response_string)
        return


    response_string = """
    
{
"access":{
    "token":{

        "id": "b591657e28e54b4ca1032cfc3e426e0a"
    }
}}
"""