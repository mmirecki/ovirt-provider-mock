from neutron.base import PostResponseBase
import json


class UpdatePorts(PostResponseBase):

    def path(self):
        return 'subnets'

    def response(self, path, content):

        content_json = json.loads(content)

        # This is the device id which will be used to identify this port in
        # subsequent requests
        print("Port device id: " + str(content_json['port']['device_id']))
        return """
{
    "subnet":
    {
        "name": "public2",
        "enable_dhcp": true,
        "network_id": "bf864bf3-81d8-438d-bf68-4b0c357309b3",
        "tenant_id": "547deac3d7f64e2688de188365a139aa",
        "dns_nameservers": [],
        "gateway_ip": "7.7.7.1",
        "ipv6_ra_mode": null,
        "allocation_pools": [{"start": "7.7.7.2", "end": "7.7.7.254"}],
        "host_routes": [],
        "ip_version": 4,
        "ipv6_address_mode": null,
        "cidr": "7.7.7.0/24",
        "id": "6ea2550b-960a-4988-97aa-892e8bbca52b",
        "subnetpool_id": null
    }
}
"""

"""
Query:
{
  "subnet" : {
    "name" : "public2",
    "cidr" : "7.7.7.0/24",
    "enable_dhcp" : true,
    "network_id" : "bf864bf3-81d8-438d-bf68-4b0c357309b3",
    "tenant_id" : "547deac3d7f64e2688de188365a139aa",
    "dns_nameservers" : [ ],
    "ip_version" : 4
  }
}



"""
