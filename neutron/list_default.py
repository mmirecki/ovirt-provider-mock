from neutron.base import ResponseBase


class ListDefault(ResponseBase):

    def path(self):
        return ''

    def response(self, path):
        return """
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
