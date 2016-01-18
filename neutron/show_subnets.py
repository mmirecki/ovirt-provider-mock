from neutron.base import ResponseBase


class ShowSubnets(ResponseBase):

    def path(self):
        return 'subnets/'

    def response(self, path):
        return """
{
    "subnet": {
        "name": "private_subnet",
        "enable_dhcp": true,
        "network_id": "59b48a4c-893c-47d2-9df3-84102329bbb9",
        "tenant_id": "472beee27f704a5b8a6f3a15fdac7ba5",
        "dns_nameservers": [],
        "gateway_ip": "10.0.0.1",
        "ipv6_ra_mode": null,
        "allocation_pools": [
        {
            "start": "10.0.0.2",
            "end": "10.0.0.254"
        }],
        "host_routes": [],
        "ip_version": 4,
        "ipv6_address_mode": null,
        "cidr": "10.0.0.0/24",
        "id": "6ed90628-5d9c-4eae-8665-0b2420e683d4",
        "subnetpool_id": null
    }
}
"""
