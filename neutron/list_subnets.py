from neutron.base import ResponseBase


class ListSubnets(ResponseBase):

    def path(self):
        return 'subnets'

    def response(self, path):
        return """
{"subnets":
[
    {
        "name": "private_subnet",
        "enable_dhcp": true,
        "network_id": "59b48a4c-893c-47d2-9df3-84102329bbb9",
        "tenant_id": "472beee27f704a5b8a6f3a15fdac7ba5",
        "dns_nameservers": [],
        "gateway_ip": "10.0.0.1",
        "ipv6_ra_mode": null,
        "allocation_pools":
        [
            {
                "start": "10.0.0.2",
                "end": "10.0.0.254"
            }
        ],
        "host_routes": [],
        "ip_version": 4,
        "ipv6_address_mode": null,
        "cidr": "10.0.0.0/24",
        "id": "6ed90628-5d9c-4eae-8665-0b2420e683d4",
        "subnetpool_id": null
    },
    {
        "name": "public_subnet",
        "enable_dhcp": false,
        "network_id": "bf864bf3-81d8-438d-bf68-4b0c357309b3",
        "tenant_id": "547deac3d7f64e2688de188365a139aa",
        "dns_nameservers": [],
        "gateway_ip": "172.24.4.225",
        "ipv6_ra_mode": null,
        "allocation_pools":
        [
            {
                "start": "172.24.4.226",
                "end": "172.24.4.238"
            }
        ],
        "host_routes": [],
        "ip_version": 4,
        "ipv6_address_mode": null,
        "cidr": "172.24.4.224/28",
        "id": "dc594048-a9e2-4ec9-9928-4157cea7e530",
        "subnetpool_id": null
    }
]}
"""
