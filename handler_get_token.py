from BaseHTTPServer import BaseHTTPRequestHandler

class GetTokenHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "Application/json")
        self.send_header("x-openstack-request-id", "req-edf1f07f-1ccf-4d42-a073-b2bd99bb9f4a")

        self.end_headers()
        self.wfile.write(self.response_string)
        return


    response_string = """
    
{
"access":{
    "token":{
       "issued_at": "2015-12-08T10:48:13.976989", 
        "expires": "2015-12-08T11:48:13Z", 
        "id": "b591657e28e54b4ca1032cfc3e426e0a", 
        "tenant":{
            "description": "admin tenant", 
            "enabled": true, 
            "id": "547deac3d7f64e2688de188365a139aa", 
            "name": "admin"
        }, 
        "audit_ids": ["TvpJO29vRryVNDJaENj-PA"]
    }, 
    "serviceCatalog": [
        {
        "endpoints": [{
            "adminURL": "http://192.168.120.151:9696", 
            "region": "RegionOne", "internalURL": "http://192.168.120.151:9696", 
            "id": "08e6708cfb9245efbf2005ceb11ced43", "publicURL": "http://192.168.120.151:9696"
        }], 
        "endpoints_links": [], 
        "type": "network", "name": "neutron"}], 
        
    "user": {
        "username": "admin", 
        "roles_links": [], 
        "id": "4588501088d94b3eb14e9608dd7833a4", 
        "roles": [{
            "name": "admin"
        }], 
        "name": "admin"
    }, 
    "metadata": {
        "is_admin": 0, 
        "roles": ["b648b417fc864686845450e2f89b8fe1"]
    }
}}
"""