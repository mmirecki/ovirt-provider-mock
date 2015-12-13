from BaseHTTPServer import BaseHTTPRequestHandler

class TestConnectionHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "Application/json")
        self.send_header("x-openstack-request-id", "req-edf1f07f-1ccf-4d42-a073-b2bd99bb9f4a")

        self.end_headers()
        
        if self.path == "" or self.path == "/" or self.path == "/v2.0" or self.path == "/v2.0/":
            self.wfile.write(self.response_string_default)
        elif self.path == "/v2.0/networks" or self.path == "/v2.0/networks/":
            self.wfile.write(self.response_string_networks)
            
        return


    response_string_default = """
{
    "resources": 
    [{
        "links": [{
            "href": "http://192.168.120.151:9696/v2.0/subnets", 
            "rel": "self"
        }], 
        "name": "subnet", 
        "collection": "subnets"
    }, 
    {
        "links": [{
            "href": "http://192.168.120.151:9696/v2.0/subnetpools", 
            "rel": "self"
        }], 
        "name": "subnetpool", 
        "collection": "subnetpools"
    }, 
    {
        "links": [{
            "href": "http://192.168.120.151:9696/v2.0/networks", 
            "rel": "self"
        }], 
        "name": "network", 
        "collection": "networks"
    },
    {
         "links": [{
             "href": "http://192.168.120.151:9696/v2.0/ports", 
             "rel": "self"
        }], 
        "name": "port", 
        "collection": "ports"
    }]
}
"""

    response_string_networks="""
{
    "networks": [
        {
            "status": "ACTIVE", 
            "subnets": ["dc594048-a9e2-4ec9-9928-4157cea7e530"], 
            "name": "public", 
            "provider:physical_network": null, 
            "admin_state_up": true, 
            "tenant_id": "547deac3d7f64e2688de188365a139aa", 
            "mtu": 0, 
            "router:external": true, 
            "shared": false, 
            "provider:network_type": "vxlan", 
            "id": "bf864bf3-81d8-438d-bf68-4b0c357309b3", 
            "provider:segmentation_id": 35
        }, 
        {
            "status": "ACTIVE", 
            "subnets": ["6ed90628-5d9c-4eae-8665-0b2420e683d4"], 
            "name": "private", 
            "provider:physical_network": null, 
            "admin_state_up": true, 
            "tenant_id": "472beee27f704a5b8a6f3a15fdac7ba5", 
            "mtu": 0, 
            "router:external": false, 
            "shared": false, 
            "provider:network_type": "vxlan", 
            "id": "59b48a4c-893c-47d2-9df3-84102329bbb9", 
            "provider:segmentation_id": 56
        }
    ]
}
"""